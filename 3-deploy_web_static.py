#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""


import os
from fabric.api import local, run, env, put
from datetime import datetime
import logging


logger = logging.getLogger('ftpuploader')
env.hosts = ['35.237.237.122', '35.237.87.28']
env.user = "ubuntu"
env.key_filename = "~/.ssh/holberton"


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    Archive:
        web_static_<year><month><day><hour><minute><second>.tgz
    Return:
        Return the archive path if the archive has been correctly generated
        Else, return None

    """
    from fabric.api import local
    from datetime import datetime

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    name = "versions/web_static_{}.tgz".format(time)
    tar_file = local("tar -cvzf {} web_static".format(name))

    if tar_file.succeeded:
        return name
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    Return:
        False if the file at the path archive_path doesn’t exist
    """
    fp = archive_path.split('/')[1]

    try:
        put(archive_path, '/tmp/{}'.format(fp))
        run('mkdir -p /data/web_static/releases/{}'.format(fp))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(fp, fp))
        run('rm /tmp/{}'.format(fp))
        run('mv -f /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}/'.format(fp, fp))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(fp))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} \
        /data/web_static/current'.format(fp))
        print('New version deployed!')
        return True

    except Exception as e:
        logger.error(str(e))
        print('New version has not been deployed...')
        return False


def deploy():
    """
    Automates the deployment of archives
    """
    dws = do_pack()
    if dws is None:
        return False
    return do_deploy(dws)
