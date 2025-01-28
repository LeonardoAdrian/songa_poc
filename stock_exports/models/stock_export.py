from odoo import models, fields


class StockExport(models.Model):
    _name = 'stock.export'
    _description = 'Modelo para gestionar informacion de exportacion'


    name = fields.Char(string='Name')
    description = fields.Char(string='Descripcion')

    date = fields.Datetime(string='Fecha')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
    country_id = fields.Many2one(comodel_name='res.country', related='partner_id.country_id', string='Pais de destino')
    country_code = fields.Char(string='Codigo de Pais de destino', related='partner_id.country_code')
    transport_type = fields.Many2one('stock.transport.type', string='Tipo de transporte')

    stock_export_lines_ids = fields.One2many(
        comodel_name='stock.export.line',
        inverse_name='stock_export_id',
        string='Productos a exportar',
    )

    status = fields.Selection(
        selection=[
            ('draft', 'Creado'),
            ('confirmed', 'Confirmado'),
            ('dispatching', 'Preparando envio'),
            ('in_transit', 'En transito'),
            ('in_custom', 'En Aduana'),
            ('delivered', 'Completado'),
            ('canceled', 'Cancelado')
        ],
        string='Estado',
        default='draft')

    departure_date = fields.Date(string='Fecha de Salida')
    arrival_date = fields.Date(string='Fecha Estimada de Llegada')
    real_arrival_date = fields.Date(string='Fecha Real de Llegada')
    total_weight = fields.Float(string='Peso Total (kg)')
    total_volume = fields.Float(string='Volumen Total (m³)')

    sale_order_id = fields.Many2one('sale.order', string='Orden de venta asociada')

    tracking_document_name = fields.Char(string='Guia')
    tracking_document_file = fields.Binary(string='Subir Documento')





