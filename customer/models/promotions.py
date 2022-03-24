from odoo import api, fields, models, tools, _

class Promotions(models.Model):
    _name = 'promotions'
    _description = 'Decription'

    name = fields.Char('Name Promotions', required=True)
    points = fields.Float('% point in Category.', required=True)
    active = fields.Boolean(string="Active", required=True)
