from odoo import api, fields, models, tools, _


class Customer(models.Model):
    _inherit = 'res.partner'
    _description = 'Decription'

    loyalty_point = fields.Float('Point Save ', readonly=1)
    loyalty_level = fields.Many2one('partner.levels', readonly=1)
