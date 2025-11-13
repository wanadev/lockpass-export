#!/usr/bin/env python3

import sys
import argparse


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="CLI tool to export LockSelf/LockPass shared passwords",
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

    print(params)  # FIXME


if __name__ == "__main__":
    main()
