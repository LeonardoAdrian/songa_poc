from openpyxl.styles.builtins import total

from odoo import models, fields


class StockExportLine(models.Model):
    _name = 'stock.export.line'
    _description = 'Modelo para gestionar cada producto que va a exportarse'

    product_id = fields.Many2one('product.product', string='Producto a exportar')
    weight = fields.Float(string='Peso total (100 kg por caja)')
    volume = fields.Float(string='Volumen (m³)')
    price = fields.Float(related='product_id.product_tmpl_id.list_price',string='Precio por Kg')

    stock_export_id = fields.Many2one('stock.export', string='Exportacion')

    arancel_id = fields.Many2one('stock.movement.arancel', string='Arancel aplicado')


    def calculate_arancel_final_price(self):
        for record in self:
            arancel_total_price = 0

            category_id = record.product_id.product_tmpl_id.categ_id
            arancel_id = self.env['stock.movement.arancel'].search([('category_id', '=', category_id.id)])
            record.arancel_id = arancel_id
            for arancel in arancel_id:
                arancel_total_price = record.price * ( record.weight / 100 ) * ( arancel.tasa / 100)

            total_price = arancel_total_price + record.price * ( record.weight / 100 )
            return total_price

