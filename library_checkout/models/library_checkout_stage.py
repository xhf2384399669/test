from odoo import fields, models


class CheckoutStage(models.Model):
    _name = 'library.checkout.stage'
    _description = 'Checkout Stage'
    _order = 'sequence,name'

    name = fields.Char()
    fold = fields.Boolean()
    sequence = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection([('new', 'New'), ('open', 'Borrowed'), ('done', 'Returned'), ('cancel', 'Cancelled')],
                             default='new', )
