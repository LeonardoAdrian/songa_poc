from odoo import models, fields


class StockMovementFeeCategory(models.Model):
    _name = 'stock.movement.fee.category'
    _description = 'Categoria de tarifa de movimiento de stock'

    name = fields.Char(string='Nombre')

    fee_ids = fields.One2many(
        comodel_name='stock.movement.fee',
        inverse_name='category_id',
        string='Tarifas & Aranceles',
    )

