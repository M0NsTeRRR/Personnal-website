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

from rest_framework import serializers
from .models import (
    Link,
    Skill,
    SkillTheme,
    SkillItem,
    Experience,
    Education,
    Language,
    Project,
    Social,
    Person,
)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class SkillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillItem
        fields = (
            'id',
            'title',
            'stars'
        )
        depth = 1


class SkillThemeSerializer(serializers.ModelSerializer):
    skillItems = SkillItemSerializer(many=True, read_only=True)

    class Meta:
        model = SkillTheme
        fields = (
            'id',
            'title',
            'skillItems'
        )


class SkillSerializer(serializers.ModelSerializer):
    skillThemes = SkillThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Skill
        fields = (
            'id',
            'title',
            'skillThemes'
        )


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = (
            'id',
            'title',
            'description',
            'url',
            'type',
            'start_date',
            'end_date'
        )


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'id',
            'title',
            'subtitle',
            'date',
            'url'
        )


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = (
            'id',
            'name',
            'level'
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'img',
            'start_date',
            'pub_date',
            'link'
        )
        depth = 1


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = (
            'id',
            'type',
            'url'
        )


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1
