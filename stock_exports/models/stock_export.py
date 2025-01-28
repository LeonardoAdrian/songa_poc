from odoo import models, fields, api


class StockExport(models.Model):
    _name = 'stock.export'
    _description = 'Modelo para gestionar informacion de exportacion'


    name = fields.Char(string='Name')
    description = fields.Char(string='Descripcion')

    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
    country_id = fields.Many2one(comodel_name='res.country', related='partner_id.country_id', string='Pais de destino')
    country_code = fields.Char(string='Codigo de Pais de destino', related='partner_id.country_code')
    transport_type = fields.Many2one('stock.transport.type', string='Tipo de transporte')
    distance = fields.Float(string='Distancia (km)')


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

    sale_order_id = fields.Many2one('sale.order', string='Orden de venta asociada')

    tracking_document_name = fields.Char(string='Guia')
    tracking_document_file = fields.Binary(string='Subir Documento')


    total_price = fields.Float(string='Precio Total')
    total_weight = fields.Float(string='Peso Total (kg)')
    total_volume = fields.Float(string='Volumen Total (m³)')

    transport_fee = fields.Float(related='transport_type.transport_fee', string='Costo del Transporte por km')

    @api.onchange('stock_export_lines_ids')
    def _compute_costos(self):
        for record in self:
            total_cost_without_trasnport_fee = 0
            total_weight = 0
            total_volume = 0
            for line in record.stock_export_lines_ids:
                total_cost_without_trasnport_fee += line.calculate_arancel_final_price()
                total_weight += line.weight
                total_volume += line.volume
            transport_fee = record.distance * record.transport_type.transport_fee
            record.total_price = transport_fee + total_cost_without_trasnport_fee
            record.total_weight = total_weight
            record.total_volume = total_volume














