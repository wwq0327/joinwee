#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""用于joinwee.com服务器应用更新"""

from fabric.api import run, cd, env
from fabric.colors import red, green

env.hosts = ['joinwee.com']
env.user = 'wyatt'
prj_path = '/home/wyatt/git/joinwee'
code_path = '/home/wyatt/git/joinwee/joinwee.org/joinwee'

def pull(br):
    print green("Checkout to %s..." % br)
    with cd(code_path):
        run("pwd")
        run("git checkout %s" % br)
        run("git pull origin %s" % br)

    print red("PULL DONE!")

def restart():
    print red("Benginning Deploy:")
    with cd(code_path):
        run("pwd")
        print green("kill django...")
        run("cat /tmp/django.pid")
        run("kill -9 `cat /tmp/django.pid`")
        print green("Start django server")
        run("pwd")
        run('source %s/bin/activate && python ./manage.py runfcgi host=127.0.0.1 port=8081 pidfile=/tmp/django.pid' % prj_path)
        
    print red("DONE!")

def migrate():
    print red("Benginning Migrate...")
    with cd(code_path):
        run("pwd")
        print green("Syanc database...")
        run("source %s/bin/activate && python ./manage.py syncdb" % prj_path)
        print green("Migration the database...")
        run("source %s/bin/activate && python ./manage.py migrate" % prj_path)

    print red("DONE!")
        

def master():
    pull("master")
    migrate()
    restart()

def dev():
    pull("dev")
    migrate()
    restart()
