# Copyright <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Videogames Cases Nelson",
    "summary": "Manage videogames",
    "version": "17.0.1.0.0",
    "category": "Videogames",
    "author": "Nelson Vera Cabrera",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/groups.xml",
        "security/ir.model.access.csv",
        "views/videogames_cases_actions.xml",
        "views/videogames_cases_views.xml",
        "data/videogames_license_nelson_data.xml",
    ],
}
