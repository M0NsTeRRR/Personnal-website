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

from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedModelAdmin
from .models import (
    Link,
    Skill,
    SkillTheme,
    SkillItem,
    Experience,
    Education,
    Language,
    Project,
    Homelab,
    Social,
    Person,
)


class LinkAdmin(NestedTabularInline):
    model = Link


class SocialAdmin(NestedTabularInline):
    model = Social
    extra = 1


class HomelabAdmin(NestedTabularInline):
    model = Homelab


class ProjectAdmin(NestedTabularInline):
    model = Project
    extra = 1


class LanguageAdmin(NestedTabularInline):
    model = Language
    extra = 1


class EducationAdmin(NestedTabularInline):
    model = Education
    extra = 1


class ExperienceAdmin(NestedTabularInline):
    model = Experience
    extra = 1


class SkillItemAdmin(NestedTabularInline):
    model = SkillItem
    extra = 1


class SkillThemeAdmin(NestedTabularInline):
    model = SkillTheme
    extra = 1
    inlines = [SkillItemAdmin]


class SkillAdmin(NestedTabularInline):
    model = Skill
    extra = 1
    inlines = [SkillThemeAdmin]


class PersonAdmin(NestedModelAdmin):
    model = Person
    inlines = [
        SocialAdmin,
        HomelabAdmin,
        ProjectAdmin,
        LanguageAdmin,
        EducationAdmin,
        ExperienceAdmin,
        SkillAdmin,
    ]


admin.site.register(Person, PersonAdmin)
admin.site.register(Link)
