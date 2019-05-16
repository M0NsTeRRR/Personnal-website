# ----------------------------------------------------------------------------
# Copyright © Ludovic Ortega, 2019
#
# Contributeur(s):
#     * Ortega Ludovic - mastership@hotmail.fr
#
# Ce logiciel, Website, est un programme informatique servant à afficher mes
# informations (CV/Portfolio) et à me joindre via un formulaire de contact.
#
# Ce logiciel est régi par la licence CeCILL soumise au droit français et
# respectant les principes de diffusion des logiciels libres. Vous pouvez
# utiliser, modifier et/ou redistribuer ce programme sous les conditions
# de la licence CeCILL telle que diffusée par le CEA, le CNRS et l'INRIA
# sur le site "http://www.cecill.info".
#
# En contrepartie de l'accessibilité au code source et des droits de copie,
# de modification et de redistribution accordés par cette licence, il n'est
# offert aux utilisateurs qu'une garantie limitée.  Pour les mêmes raisons,
# seule une responsabilité restreinte pèse sur l'auteur du programme,  le
# titulaire des droits patrimoniaux et les concédants successifs.
#
# A cet égard  l'attention de l'utilisateur est attirée sur les risques
# associés au chargement,  à l'utilisation,  à la modification et/ou au
# développement et à la reproduction du logiciel par l'utilisateur étant
# donné sa spécificité de logiciel libre, qui peut le rendre complexe à
# manipuler et qui le réserve donc à des développeurs et des professionnels
# avertis possédant  des  connaissances  informatiques approfondies.  Les
# utilisateurs sont donc invités à charger  et  tester  l'adéquation  du
# logiciel à leurs besoins dans des conditions permettant d'assurer la
# sécurité de leurs systèmes et ou de leurs données et, plus généralement,
# à l'utiliser et l'exploiter dans les mêmes conditions de sécurité.
#
# Le fait que vous puissiez accéder à cet en-tête signifie que vous avez
# pris connaissance de la licence CeCILL, et que vous en avez accepté les
# termes.
# ----------------------------------------------------------------------------

FROM python:3.7-alpine as build

MAINTAINER Ludovic Ortega mastership@hotmail.fr

# update package
RUN apk update

# install git
RUN apk add git

# download website project
RUN git clone https://github.com/M0NsTeRRR/website

# copy file to /app/
RUN mkdir -p /app/backend/ && mv website/backend/* /app/backend/

# remove useless file
RUN rm -Rf ./website /app/backend/Dockerfile

# install dependencies
RUN pip3 install -r ./app/backend/requirements.txt

FROM python:3.7-alpine

# update package
RUN apk update

# install gunicorn
RUN pip3 install gunicorn

# copy backend
COPY --from=build /app/backend/ /app/backend/

# copy python library
COPY --from=build  /usr/local/lib/python3.7/site-packages/ /usr/local/lib/python3.7/site-packages/

# set workdir
WORKDIR /app/backend/

# set environment variables
ENV SECRET_KEY SECRET_KEY
ENV EMAIL_HOST EMAIL_HOST
ENV EMAIL_PORT EMAIL_PORT
ENV EMAIL_USE_TLS EMAIL_USE_TLS
ENV EMAIL_USE_SSL EMAIL_USE_SSL
ENV EMAIL_HOST_USER EMAIL_HOST_USER
ENV EMAIL_HOST_PASSWORD EMAIL_HOST_PASSWORD
ENV EMAIL_RECEIVER EMAIL_RECEIVER

# expose port
EXPOSE 8000

# create database
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]