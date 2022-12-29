#!/usr/bin/env bash
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder using the function do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    run('mkdir -p versions')
    time= datetime.now().strftime("%Y%m%d%H%M%S")
    name = "webs_tatic_{}.tgx".format(time)
    fname = "versions/{}".format(name)
    archive_path = local("tar -cvzf {} webstatic/".format(fname))
    if archive_path:
        return (archive_path)
    else:
        return None
