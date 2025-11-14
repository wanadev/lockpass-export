#!/usr/bin/env python3

import argparse
import io
import json
import os
import pathlib
import secrets
import sys
import typing
import urllib.parse
import urllib.request
import zipfile


__application_name__ = "LockPass Export"
__application_id__ = "org.wanadev.lockpass-export"
__version__ = "1.0.0"


def lockself_api_generate_export_link(
    instance_url: str,
    auth_token: str,
    ls_token: str,
    organisation_id: int,
    zip_password: str,
) -> str:
    endpoint_url = urllib.parse.urljoin(instance_url, "api-key/download/generate/token")
    headers = {
        "User-Agent": "/".join([__application_id__, __version__]),
        "Content-Type": "application/json",
        "X-Auth-Token": auth_token,
        "X-Ls-Token": ls_token,
    }
    payload = {
        "method": "downloadGlobalExport",
        "organizationId": organisation_id,
        "zipPassword": zip_password,
    }

    request = urllib.request.Request(
        endpoint_url,
        method="POST",
        headers=headers,
        data=json.dumps(payload).encode("UTF-8"),
    )
    response = urllib.request.urlopen(request)

    if response.code != 200:
        raise Exception("API returned an error (HTTP status code: %i)" % response.code)

    data = json.loads(response.read())

    if "link" not in data:
        raise Exception("Unexpected response from the API (missing link)")

    return data["link"]


def lockself_api_download_zip(export_url: str) -> bytes:
    headers = {
        "User-Agent": "/".join([__application_id__, __version__]),
    }

    request = urllib.request.Request(
        export_url,
        method="GET",
        headers=headers,
    )
    response = urllib.request.urlopen(request)

    if response.code != 200:
        raise Exception("API returned an error (HTTP status code: %i)" % response.code)

    return response.read()


def extract_zip_to_folder(
    zip_file: typing.BinaryIO,
    zip_password: bytes,
    output_folder: str | os.PathLike,
) -> None:
    with zipfile.ZipFile(zip_file) as z:
        z.extractall(output_folder, pwd=zip_password)


def generate_password(length: int = 64) -> str:
    return secrets.token_urlsafe(length)


def main(args: list = sys.argv[1:]) -> None:
    parser = argparse.ArgumentParser(
        description="CLI tool to export LockSelf/LockPass shared passwords",
    )

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%s v%s" % (__application_name__, __version__),
    )
    parser.add_argument(
        "-u",
        "--url",
        help="URL of your LockPass instance (e.g. 'https://yourcompany.lockself-cloud.com')",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-a",
        "--auth-token",
        help="API Auth Token",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-l",
        "--ls-token",
        help="API LS Token",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-i",
        "--organisation-id",
        help="ID of the organisation to export (default: 1)",
        type=int,
        default=1,
    )

    parser.add_argument(
        "FOLDER",
        help="Folder where files will be written (created if not exists).",
        type=str,
    )

    params = parser.parse_args(args)
    zip_password = generate_password()

    export_url = lockself_api_generate_export_link(
        params.url,
        params.auth_token,
        params.ls_token,
        params.organisation_id,
        zip_password,
    )

    export_zip_bytes = lockself_api_download_zip(export_url)
    export_zip_io = io.BytesIO(export_zip_bytes)

    output_folder = pathlib.Path(params.FOLDER)
    output_folder.mkdir(parents=True, exist_ok=True)

    extract_zip_to_folder(export_zip_io, zip_password.encode("UTF-8"), output_folder)


if __name__ == "__main__":
    main()
