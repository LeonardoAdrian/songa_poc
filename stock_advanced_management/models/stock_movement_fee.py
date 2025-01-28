from odoo import models, fields


class StockMovementFee(models.Model):
    _name = 'stock.movement.fee'
    _description = 'Tarifas para movimientos de inventario'
    name = fields.Char(string='Nombre de la Tarifa', required=True)

    fecha_vigencia = fields.Date(string='Fecha de Vigencia', required=True, default=fields.Date.today())
    active = fields.Boolean(string='Activo', default=True)
    movement_type = fields.Selection([
        ('exportacion', 'Exportacion'),
        ('importacion', 'Importacion'),
    ], string='Tipo')

    transport_id = fields.Many2one(
        comodel_name='stock.transport.type',
        string='Trasporte Asociado',
    )

    costo = fields.Float(related='transport_id.transport_fee', string='Costo')

