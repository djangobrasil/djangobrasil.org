# -*- coding: utf-8 -*-
import os
from fabric.api import cd, env, run


env.project_root = "/home/djangobrasil/djangobrasil.org/"
env.app_root = env.project_root + "/src/djangobrasil"
env.virtualenv = "/home/djangobrasil/.virtualenvs/djangobrasil"


def update():
    with cd(env.project_root):
        run("git pull")


def deps():
    run("%(virtualenv)s/bin/pip install -r %(project_root)s/requirements.txt" % env)


def start():
    with cd(env.app_root):
        run('%(virtualenv)s/bin/gunicorn_django -p gunicorn.pid --bind=127.0.0.1:7777--daemon --workers=3' % env)


def stop():
    run('kill -TERM `cat %(app_root)s/gunicorn.pid`' % env)


def reload():
    run('kill -HUP `cat %(app_root)s/gunicorn.pid`' % env)


def clean():
    with cd(env.app_root):
        run("find . -name \"*.pyc\" | xargs rm -f ")


def deploy():
    update_app()
    deps()
    clean()
    reload()
