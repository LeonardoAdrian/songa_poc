from odoo import models, fields


class StockExportLine(models.Model):
    _name = 'stock.export.line'
    _description = 'Modelo para gestionar cada producto que va a exportarse'

    product_id = fields.Many2one('product.product', string='Producto a exportar')
    weight = fields.Float(string='Peso total (kg)')
    volume = fields.Float(string='Volumen (m³)')
    price = fields.Float(related='product_id.product_tmpl_id.list_price',string='Precio por Kg')

    stock_export_id = fields.Many2one('stock.export', string='Exportacion')

    exports_fee_ids = fields.Many2many('stock.exports.fee', string='Tarifas de exportacion')

