#!/usr/bin/env bash
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

    from fabric.operations import local, run, put, env
    from datetime import datetime 

    time = datetime.now().strftime("%Y%m%d%H%M%S%f")
    name = "./version/web_static_{}".format(time)

    tar_file = local("tar -czfv {} web_static".format(name))

    if tar_file.succeeded:
        return name
    else:
        return None


