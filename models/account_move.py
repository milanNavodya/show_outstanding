from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    outstanding = fields.Float("Outstanding")

    def _compute_outstanding(self):
        for rec in self:
            if rec.partner_id and rec.move_type == 'out_invoice':
                if rec.partner_id.property_account_receivable_id:
                    pass
                else:
                    rec.outstanding = 0
            else:
                rec.outstanding = 0
