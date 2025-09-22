# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class IrActionReport(models.Model):
    _inherit = "ir.actions.report"

    @api.model
    def public_render_qweb_pdf(self, report_ref, res_ids=None, data=None):
        """Render a QWeb PDF report.

        Args:
            report_ref (str): The report reference.
            res_ids (list, optional): The IDs of the records to print. Defaults to None.
            data (dict, optional): Additional data to pass to the report. Defaults to None.

        Returns:
            bytes: The rendered PDF report.
            Example:
                To render a PDF report for a specific model:

                    report_ref = 'module_name.report_template_id'
                    res_ids = [1, 2, 3]
                    pdf_bytes = self.env['ir.actions.report'].public_render_qweb_pdf(report_ref, res_ids)
                    # pdf_bytes now contains the base64-encoded PDF content
        """
        pdf_content = self._render_qweb_pdf(report_ref, res_ids=res_ids, data=data)
        return base64.b64encode(pdf_content)
