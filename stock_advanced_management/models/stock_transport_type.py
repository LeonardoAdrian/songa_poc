from odoo import models, fields


class StockTransportType(models.Model):
    _name = 'stock.transport.type'
    _description = 'Medio de transporte para exportaciones e importaciones'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Categoria',
    )

    name = fields.Char(string='Nombre')
    maximum_weight_allowed = fields.Float(string='Peso Total (kg) permitido')
    transport_fee = fields.Float(string='Costo del Transporte por kg')
