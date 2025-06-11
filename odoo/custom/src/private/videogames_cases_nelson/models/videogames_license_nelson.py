from odoo import fields, models


# Class to manage licenses related to videogames #
class VideogamesLicenseNelson(models.Model):
    _name = "videogames.license.nelson"
    _description = "Videogames License"

    # Fields #
    name = fields.Char(string="Name", required=True)
    reference = fields.Char(string="Reference")
    partner_id = fields.Many2one("res.partner", string="Partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
