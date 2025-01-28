from odoo import models, fields


class StockMovementFee(models.Model):
    _name = 'stock.movement.fee'
    _description = 'Tarifas para movimientos de inventario'

    name = fields.Char(string='Nombre')
    movement_type = fields.Selection([
        ('exportacion', 'Exportacion'),
        ('importacion', 'Importacion'),
    ], string='Tipo')

    category_id = fields.Many2one(
        comodel_name='stock.movement.fee.category',
        string='Categoria',
    )