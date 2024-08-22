#!/usr/bin/env bash

# Install nginx web server and start it
# Install Nginx if it is not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get -y update
    apt-get -y install nginx
    service nginx start
fi

# Firewall setting: Allow Nginx to serve on HTTP
ufw allow 'Nginx HTTP'

# Override the default index file served as home page
[ ! -e /var/www/html/index.nginx-debian-bk.html ] && cp /var/www/html/index.nginx-debian.html /var/www/html/index.nginx-debian-bk.html
echo "Hello World!" | sudo tee /var/www/html/index.html

CONFIG_FILE="/etc/nginx/sites-available/default"

if ! grep -q "location /redirect_me" "$CONFIG_FILE"; then
    sed -i "/server_name _;/a location /redirect_me {\n return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n}" "$CONFIG_FILE"
fi

# Restart nginx after new configurations
service nginx restart