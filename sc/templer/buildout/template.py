# -*- coding:utf-8 -*-

from random import choice

from string import digits
from string import letters

from templer.core.base import BaseTemplate
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import StringVar

BASE = digits + letters


class Buildout(BaseTemplate):

    summary = "Create a simple buildout"
    help = """This template allows you to create a buildout"""

    category = "Simples Consultoria - Buildout"

    use_cheetah = True

    required_templates = []
    default_required_structures = ['bootstrap', ]
    _template_dir = "templates/buildout"


class FrontEndBuildout(Buildout):

    summary = "Create a Frontend buildout with Nginx, Varnish and Repoze"
    help = """This template creates a buildout for a frontend server running
              Nginx, Varnishm Repoze.
           """

    required_templates = []
    _template_dir = "templates/frontend_buildout"

    vars = [
        StringVar(
            'url',
            'URL (without http://)',
            default='',
            modes=(EASY, EXPERT),
           )]

    def gen_seed(self, size=19):
        ''' Generate a seed to the cookie mechanism '''
        seed = [choice(BASE) for i in range(0, size)]
        return ''.join(seed)

    def check_vars(self, vars, cmd):
        resp = super(FrontEndBuildout, self).check_vars(vars, cmd)
        resp['seed'] = self.gen_seed()
        return resp


class PloneBuildout(Buildout):

    summary = "Create a Plone buildout"
    help = """This template allows you to create a Plone buildout"""

    required_templates = []
    _template_dir = "templates/plone_buildout"

    vars = [
        StringVar(
            'plone_version',
            'Plone version',
            default='4.1',
            modes=(EASY, EXPERT),
           )]
