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

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    TYPE_CHOICE = (
        ('github', 'Github'),
        ('website', 'Website'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, default='github')

    def __str__(self):
        return self.title


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=100)
    city_residence = models.CharField(max_length=100)
    presentation = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to='cv/person', blank=True)
    actual_position = models.OneToOneField(Link, on_delete=models.PROTECT)
    cv_url = models.FileField(upload_to='cv/person', blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    person = models.ForeignKey(Person, related_name='skills', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SkillTheme(models.Model):
    skill = models.ForeignKey(Skill, related_name='skillThemes', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class SkillItem(models.Model):
    skill_theme = models.ForeignKey(SkillTheme, related_name='skillItems', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    stars = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.title


class Experience(models.Model):
    TYPE_CHOICE = (
        ('work', 'Work'),
        ('volunteer', 'Volunteer'),
    )
    person = models.ForeignKey(Person, related_name='experiences', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=200, blank=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, default='work')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    person = models.ForeignKey(Person, related_name='educations', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Language(models.Model):
    person = models.ForeignKey(Person, related_name='languages', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Social(models.Model):
    person = models.ForeignKey(Person, related_name='socials', on_delete=models.CASCADE)
    TYPE_CHOICE = (
        ('github', 'Github'),
        ('linkedin', 'Linkedin'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICE, default='github')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.url


class Project(models.Model):
    person = models.ForeignKey(Person, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='cv/projects', blank=True)
    link = models.OneToOneField(Link, on_delete=models.PROTECT)
    start_date = models.DateField()
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Homelab(models.Model):
    person = models.OneToOneField(Person, related_name='homelab', on_delete=models.CASCADE)
    rack = models.ImageField(upload_to='cv/homelab', blank=True)
    architecture = models.ImageField(upload_to='homelab', blank=True)
