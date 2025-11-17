LockPass Export
===============

|Github| |Discord| |PYPI Version| |Build Status| |Black| |License|

LockPass Export is a CLI tool to export shared password from LockSelf's LockPass password manager.


Prerequisite
------------

* Python >= 3.10 (no third-party dependencies)
* A LockPass instance with API option enabled
* An API account with moderator permissions

See `LockSelf documentation <https://support.lockself.com/hc/fr/articles/4412367678226-Qu-est-ce-que-l-API-LockSelf>`__ for more information about the API.


Install
-------

Standalone script
~~~~~~~~~~~~~~~~~

Just use the ``lockpass_export.py`` script from this repository, it works without any dependency beside Python itself.

To run the script, use the following command::

    python3 lockpass_export.py --help


From PyPI
~~~~~~~~~

To install from PyPI, be sure you have a complete Python 3 installation. On Debian and Ubuntu run the following command::

    apt install python3 python3-dev python3-venv

Then create a virtualenv::

    python3 -m venv /opt/lockpass-export.venv

and install LockPass Export inside it::

    /opt/lockpass-export.venv/bin/pip install lockpass-export

To run the software, use the following command::

    /opt/lockpass-export.venv/bin/lockpass-export --help


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

* **v1.0.0:**

  * Initial release


.. |Github| image:: https://img.shields.io/github/stars/wanadev/lockpass-export?label=Github&logo=github
   :target: https://github.com/wanadev/lockpass-export
.. |Discord| image:: https://img.shields.io/badge/chat-Discord-8c9eff?logo=discord&logoColor=ffffff
   :target: https://discord.gg/BmUkEdMuFp
.. |PYPI Version| image:: https://img.shields.io/pypi/v/lockpass-export.svg
   :target: https://pypi.python.org/pypi/lockpass-export
.. |Build Status| image:: https://github.com/wanadev/lockpass-export/actions/workflows/python-ci.yml/badge.svg
   :target: https://github.com/wanadev/lockpass-export/actions
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://black.readthedocs.io/en/stable/
.. |License| image:: https://img.shields.io/pypi/l/lockpass-export.svg
   :target: https://github.com/wanadev/saltimbanque/blob/master/COPYING
