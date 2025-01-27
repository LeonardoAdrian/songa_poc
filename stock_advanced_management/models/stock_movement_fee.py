from odoo import models, fields


class StockMovementFee(models.Model):
    _name = 'stock.movement.fee'
    _description = 'Tarifas para movimientos de inventario'
    name = fields.Char(string='Nombre de la Tarifa', required=True)
    costo = fields.Float(string='Costo', required=True, help="Costo fijo.")
    fecha_vigencia = fields.Date(string='Fecha de Vigencia', required=True, default=fields.Date.today())
    active = fields.Boolean(string='Activo', default=True)
    movement_type = fields.Selection([
        ('exportacion', 'Exportacion'),
        ('importacion', 'Importacion'),
    ], string='Show status')

    category_id = fields.Many2one(
        comodel_name='stock.movement.fee.category',
        string='Categoria',
    )