# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def create_invoices_wrapper(self, grouped=False):
        """Wrapper for the private _create_invoices method.
        :param bool grouped: if True, create one invoice for all orders related to same customer and same invoicing address
        """
        invoices = self._create_invoices(final=True, grouped=not grouped)
        return invoices.ids
