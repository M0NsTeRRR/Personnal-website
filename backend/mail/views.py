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

import os

from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import MailForm
import json


class MailViewset(APIView):
    @classmethod
    def post(self, request, format=None):
        """
        Create and send an email
        """

        form = MailForm(json.loads(request.body.decode('utf-8')))

        if form.is_valid():
            try:
                html_message = render_to_string('mail/mail_template.html', {'name': form.cleaned_data['name'], 'email': form.cleaned_data['email'], 'subject': form.cleaned_data['subject'], 'message': form.cleaned_data['message']})
                plain_message = strip_tags(html_message)
                send_mail('Contact form ludovic-ortega.adminafk.fr', plain_message, os.environ['EMAIL_HOST_USER'], [os.environ['EMAIL_RECEIVER']], html_message=html_message)
                send_mail('Message sent on ludovic-ortega.adminafk.fr', plain_message, os.environ['EMAIL_HOST_USER'], [form.cleaned_data['email']], html_message=html_message)
            except Exception as e:
                return Response({"success": False, "message": "Something wrent wrong. Sorry for inconveniance, try again later."})
            return Response({"success": True, "message": "Success ! Your Email has been sent, if your request can't wait, you can also reach me on my social media accounts."})
        else:
            return Response({"success": False, "message": "Make sure all fields are entered and valid."})
