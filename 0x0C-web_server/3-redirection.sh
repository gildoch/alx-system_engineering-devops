#!/usr/bin/env bash

# Install nginx web server and start it
apt-get -y update
apt-get -y install nginx
service nginx start

# Firewall setting: Allow Nginx to serve on HTTP
ufw allow 'Nginx HTTP'

# Override the default index file served as home page
echo "Hello World!" >> /var/www/html/index.html

#Give the user  ownership to website files
sudo chown -R "$USER":"$USER" /var/www/html
sudo chmod -R 755 /var/www

# Redirect to /redirect_me to a youtube video
sed -i '37i\rewrite ^/redirect_me https://http.dev/404 permanent;' /etc/nginx/sites-available/default

# Restart nginx after new configurations
service nginx restart