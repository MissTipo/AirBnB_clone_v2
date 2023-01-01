#!/usr/bin/python3

"""
A script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
env.hosts = ['54.90.55.176', '54.144.155.28']


def do_deploy(archive_path):
    """
    distributes an archive to your web servers,
    using the function do_deploy if not archive_path:
    """
    if not archive_path:
        return False
    # Upload the archive to the /tmp/ directory of the web server
    with cd('/tmp'):
        upload = put(archive_path, '/tmp/')
        print(upload)
    run('mkdir -p /data/web_static/releases/')
    file_name = archive_path.split('/')[-1]
    # return filename without the extension
    file = file_name.split('.')[0]
    # Create a subdirectory
    run('mkdir -p /data/web_static/releases/{}'.format(file))
    # tf = '/tmp/{}'
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
        .format(file_name, file))
    # delete the uploaded .tgz archive from the /tmp/ directory on the
    run('rm /tmp/{}'.format(file_name))
    # des = '/data/web_static/releases/{}'
    run('mv /data/web_static/releases/{}/web_static/* '
        '/data/web_static/releases/{}'.format(file, file))
    run('rm -rf /data/web_static/current')
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(file))
