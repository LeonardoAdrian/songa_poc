from odoo import models, fields


class StockMovementFeeCategory(models.Model):
    _inherit = 'stock.movement.fee.category'
    _description = 'Categoria de tarifa de movimiento de stock'

    fee_ids = fields.One2many(
        comodel_name='stock.movement.fee',
        inverse_name='category_id',
        string='Tarifas & Aranceles',
    )

