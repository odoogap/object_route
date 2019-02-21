# -*- coding: utf-8 -*-
from odoo import models, fields, _


class IrActionsActWindow(models.Model):
    _inherit = 'ir.actions.act_window'

    in_route = fields.Char("In Route", index=True)

    _sql_constraints = [
        ('in_route_uniq', 'unique (in_route)', _('Name of the in_route must be unique!')),
    ]
