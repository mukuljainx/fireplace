from fabric.api import local


def pylint():
    local("cd ..;export DJANGO_SETTINGS_MODULE=zamboni/settings_local;"
        "export PYTHONPATH=zamboni/apps:zamboni/lib;"
        "pylint --rcfile zamboni/scripts/pylintrc -fparseable zamboni",
        capture=False)

def pep8():
    local("pep8 --repeat --ignore E221"
        " --exclude *.sh,*.html,*.json,*.txt,*.pyc,.DS_Store,README,"
        "migrations,sphinxapi.py"
        " apps", capture=False)


def test():
    local("python manage.py test --noinput --logging-clear-handlers",
          capture=False)
