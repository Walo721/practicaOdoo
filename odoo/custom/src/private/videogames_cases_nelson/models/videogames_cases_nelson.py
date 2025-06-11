from odoo import fields, models


# Class to manage videogames #
class VideogamesCasesNelson(models.Model):
    _name = "videogames.cases.nelson"
    _description = "Videogames cases"

    # Fields #
    name = fields.Char(string="Name")
    description = fields.Text(string="Description")
    release_date = fields.Date(string="Release date")
    developer = fields.Char(string="Developer")
    publisher = fields.Char(string="Publisher")
    multiplayer = fields.Boolean(string="Multiplayer")
    status = fields.Selection(
        [
            ("not_played", "Not played"),
            ("in_progress", "In progress"),
            ("completed", "Completed"),
        ],
        string="Status",
        default="not_played",
    )
    user_id = fields.Many2one("res.users", string="User")
    sequence = fields.Integer("Sequence")
    notes = fields.Html("Notes")

    # Functions to modify the status value #
    def action_not_played(self):
        self.status = "not_played"

    def action_in_progress(self):
        self.status = "in_progress"

    def action_completed(self):
        self.status = "completed"
