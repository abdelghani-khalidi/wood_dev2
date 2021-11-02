from odoo import api, fields, models


import logging
_logger = logging.getLogger(__name__)



class cate_y(models.Model):
    _inherit = "planning.role"

    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.company)