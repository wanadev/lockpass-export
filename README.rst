LockPass Export
===============

LockPass Export is a CLI tool to export shared password from LockSelf's LockPass password manager.


Prerequisite
------------

* A LockPass instance with API option enabled
* An API account with moderator permissions
* Python >= 3.10 (no third-party dependencies)


Install
-------

Just use the ``lockpass_export.py`` script from this repository.


Usage
-----

::

    usage: lockpass_export.py [-h] [-V] -u URL -a AUTH_TOKEN -l LS_TOKEN [-i ORGANISATION_ID]
                              FOLDER

    CLI tool to export LockSelf/LockPass shared passwords

    positional arguments:
      FOLDER                Folder where files will be written (created if not exists).

    options:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -u, --url URL         URL of your LockPass instance (e.g. 'https://yourcompany.lockself-
                            cloud.com')
      -a, --auth-token AUTH_TOKEN
                            API Auth Token
      -l, --ls-token LS_TOKEN
                            API LS Token
      -i, --organisation-id ORGANISATION_ID
                            ID of the organisation to export (default: 1)

Example::

    python3 lockpass_export.py \
        --url https://mycompany.lockself-cloud.com \
        --auth-token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
        --ls-token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
        ./myexport/


Development
-----------

Install dev dependencies::

    python3 -m venv __env__
    __env__/bin/pip install -e .[dev]

Lint::

    __env__/bin/nox -s lint

Fix coding style::

    __env__/bin/nox -s black_fix



Changelog
---------

* **[NEXT]** (changes on master, but not released yet):

  * Nothing yet ;)
