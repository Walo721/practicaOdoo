from odoo import fields, models


# Class to manage videogames developers #
class VideogamesDeveloperNelson(models.Model):
    _name = "videogames.developer.nelson"
    _description = "Videogames Developers"
# Fields #
    name = fields.Char('Name')
    phone_number = fields.Char('Phone number')
    email = fields.Char('Email')
    employed = fields.Selection([
        ('Yes', 'yes'),
        ('No','no')
    ], string='Currently employed')
