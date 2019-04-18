This is my own website :)

# This tool uses :

* [Django](https://twig.symfony.com/) - Python web framework
* [Django REST framework](https://www.django-rest-framework.org/) - Python REST framework for Django
* [Vue.js](https://vuejs.org/) - Progressive framework
* [Vuetify](https://vuetifyjs.com/en/) - Component framework for Vue.js
* [Font Awesome](https://fontawesome.com/) - Icon library
* [Animate.css](https://daneden.github.io/animate.css/) - CSS library

# Requirements

- Nginx
- Docker

# Install

- Put Nginx configuration `/etc/nginx/sites-available/adminafk.fr`
- Create the symlink `ln -s /etc/nginx/sites-available/adminafk.fr /etc/nginx/sites-enabled/adminafk.fr`
- Use certbot & let's encrypt for HTTPS and to force redirection HTTP to HTTPS `certbot --nginx -d adminafk.fr -d admin.adminafk.fr -d api.adminafk.fr -d ludovic-ortega.adminafk.fr`
- Restart Nginx `systemctl restart nginx`

#### Frontend

- Build the container : `docker build -t frontend .`
- Deploy the container `docker run -d --name frontend --restart=always --publish 8080:80 frontend`

#### Backend

- Create this directories (must be empty) `/var/www/adminafk.fr/static`
- Put the secret key on the dockerfile `ENV SECRET_KEY=MY_SECRET_KEY`
- Build the container `docker build -t backend .`
- Deploy the container `docker run -d --name backend --restart=always -p 8000:8000 -v /var/www/adminafk.fr/static:/app/backend/static backend`
- Collect static files `docker exec -it backend python3 manage.py collectstatic`
- Create a SuperAdmin for Admin : 
    * `docker exec -it backend /bin/sh`  
    * `docker exec -it backend python3 manage.py createsuperuser`  

#### Add infos

- Go on admin and create a person on Admin or replace the database by another database

# Usage guide

- Access to website :
    * adminafk.fr
    * ludovic-ortega.adminafk.fr

- Access to API :
    * admin.adminafk.fr
    
- Access to admin :
    * admin.adminafk.fr

# Licence

The code is under CeCILL license.

You can find all details here: http://www.cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2019

Contributor(s):

-Ortega Ludovic - mastership@hotmail.fr
