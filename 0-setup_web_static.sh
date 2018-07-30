#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static AirBnB


sudo apt-get update -y
sudo apt-get install nginx -y

# Make directories  
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create temp html page
sudo echo -e "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link between current and test
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current 

# Give ownership of the /data/ folder to the ubuntu user AND group 
sudo chown -R ubuntu:ubuntu /data/      

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
static="\\\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n}"
sudo sed -i "40i $static" /etc/nginx/sites-enabled/default

sudo service nginx restart