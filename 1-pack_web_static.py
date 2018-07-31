#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo
"""


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

if __name__ == "__main__":
    do_pack()
