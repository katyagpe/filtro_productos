# -*- coding: utf-8 -*-
#from odoo import models, api, fields
import logging

from openerp import api, fields, models, _ 
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF


# Este lo usamos para realizar las pruebas
_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _name = 'sale.order.line'
    _inherit = 'sale.order.line'

    product_id = fields.Many2one('product.product', string='Product', domain="[('company_id', '=', parent.company_id)]", change_default=True, ondelete='restrict', required=True)