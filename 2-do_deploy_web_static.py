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
        run('mv -f /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'\
            .format(fp, fp))
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
