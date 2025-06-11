from odoo import fields, models


class VideogamesLicenseNelson(models.Model):
    _name = "videogames.license.nelson"
    _description = "Videogames License"

    name = fields.Char(string="Name", required=True)
    reference = fields.Char(string="Reference")
    partner_id = fields.Many2one("res.partner", string="Partner")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
