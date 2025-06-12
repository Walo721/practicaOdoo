from odoo import fields, models


# Class to manage videogames #
class VideogamesCasesTagNelson(models.Model):
    _name = "videogames.cases.tag.nelson"
    _description = "Videogames cases tags"

    name = fields.Char(string='Name', required=True)
