[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43b2c47c6ab34d00ae4970b11b111156)](https://app.codacy.com/app/M0NsTeRRR/Personnal-website?utm_source=github.com&utm_medium=referral&utm_content=M0NsTeRRR/Personnal-website&utm_campaign=Badge_Grade_Dashboard)
[![Docker Automated build](https://img.shields.io/docker/cloud/automated/monsterrr/personnal-website?style=flat-square)](https://hub.docker.com/r/monsterrr/personnal-website)
[![Docker Build Status](https://img.shields.io/docker/cloud/build/monsterrr/personnal-website?style=flat-square)](https://hub.docker.com/r/monsterrr/personnal-website)

This is my own website :)

# This tool uses :

* [Django](https://twig.symfony.com/) - Python web framework
* [Django REST framework](https://www.django-rest-framework.org/) - Python REST framework for Django
* [Vue.js](https://vuejs.org/) - Progressive framework
* [Vuetify](https://vuetifyjs.com/en/) - Component framework for Vue.js
* [Font Awesome](https://fontawesome.com/) - Icon library
* [Animate.css](https://daneden.github.io/animate.css/) - CSS library

# Dev

## Requirements

- Python >= 3.7
- Pip3
- Node.js >= 8.9
- npm
- Vue CLI 3

#### Frontend

In frontend/src/store/ApiConfig.js change `baseURL` of Axios request

In frontend directory run `npm install`

In frontend directory run `npm run serve`

#### Backend

In `backend/config/settings/__init__.py` change import `production` to `dev`

In backend directory run `python3 manage.py runserver`

# Production

-> https://github.com/M0NsTeRRR/Personnal-docker-config/tree/master/personnal-website

# Licence

The code is under CeCILL license.

You can find all details here: https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2019

Contributor(s):

-Ortega Ludovic - mastership@hotmail.fr
