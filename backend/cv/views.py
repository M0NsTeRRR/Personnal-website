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

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Person
from .serializers import (
    PersonSerializer,
    LanguageSerializer,
    ExperienceSerializer,
    EducationSerializer,
    ProjectSerializer,
    SocialSerializer,
    SkillSerializer,
)


class PersonViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Retrieve a Person
    """

    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get']

    @action(detail=True)
    def languages(self, request, pk=None):
        """
        Retrieve Languages of a Person
        """

        person = self.get_object()
        serializer = LanguageSerializer(person.languages.all(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def experiences(self, request, pk=None):
        """
        Retrieve Experiences of a Person
        """

        person = self.get_object()
        serializer = ExperienceSerializer(person.experiences.all(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def educations(self, request, pk=None):
        """
        Retrieve Educations of a Person
        """

        person = self.get_object()
        serializer = EducationSerializer(person.educations.all(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def skills(self, request, pk=None):
        """
        Retrieve Skills of a Person
        """

        person = self.get_object()
        serializer = SkillSerializer(person.skills.all(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def projects(self, request, pk=None):
        """
        Retrieve Projects of a Person
        """

        person = self.get_object()
        serializer = ProjectSerializer(person.projects.all(), many=True)
        return Response(serializer.data)

    @action(detail=True)
    def socials(self, request, pk=None):
        """
        Retrieve Social Networks of a Person
        """

        person = self.get_object()
        serializer = SocialSerializer(person.social.all(), many=True)
        return Response(serializer.data)
