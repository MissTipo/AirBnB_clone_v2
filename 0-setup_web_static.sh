#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static

#install nginx
sudo apt-get update -y
sudo apt-get install nginx -y

#create neccessary folders
if [ -d "/data/web_static/shared/" ]
then
	echo "/data/web_static/shared/ already exist"
else
	sudo mkdir -p '/data/web_static/shared/'
fi

if [ -d "/data/web_static/releases/test" ]
then
        echo "/data/web_static/releases/test already exist"
else
        sudo mkdir -p '/data/web_static/releases/test'
fi

if [ -f "/data/web_static/releases/test/index.html" ]
then
        echo "/data/web_static/releases/test/index.html already exist"
else
        sudo touch '/data/web_static/releases/test/index.html'
fi

# index.html message
sudo echo "Welcome, this is $(hostname) server" |sudo tee /data/web_static/releases/test/index.html

# creates symbolic link
#if [ -d "/data/web_static/current" ]
#then
#	sudo rm -rf "/data/web_static/current already exist"
#fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ownership
sudo chown -hR ubuntu:ubuntu /data/

# configuration to serve the content
sudo sed -i "19i\ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-enabled/default

# restart nginx server
sudo service nginx restart
