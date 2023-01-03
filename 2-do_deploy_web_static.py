#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""
from fabric.api import *
from datetime import datetime


env.hosts = ['54.90.55.176', "54.144.155.28"]


def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static"""
    if not archive_path:
        return False
    # Upload to /tmp/ in the server
    # put(archive_path, "/tmp/")
    with cd("/tmp/"):
        res = put(archive_path, "/tmp/")
        print(res)

    # Make directory for the file extraction
    run("mkdir -p /data/web_static/releases/")

    # GEt the file name
    file_name = archive_path.split("/")[-1]

    # Extract the file from archive
    remote_name = file_name.split(".")[0]
    run("mkdir -p /data/web_static/releases/{}".format(remote_name))
    run("tar -xzf /tmp/{} -C /data/web_static/releases/{}"
        .format(file_name, remote_name))

    # Delete the archive from the web serve
    run("rm /tmp/{}".format(file_name))

    # Move file out of web_static
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(remote_name, remote_name))

    # Delete the symbolic link
    run("rm -rf /data/web_static/current")

    # Create a new the symbolic link
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(remote_name))
