from openpyxl.styles.builtins import total

from odoo import models, fields


class ImportLine(models.Model):
    _name = 'stock.import.line'
    _description = 'Modelo para gestionar cada producto que va a importarse'

    product_id = fields.Many2one('product.product', string='Producto a importar')
    quantity = fields.Float(string='Cantidad')
    price = fields.Float(related='product_id.product_tmpl_id.list_price',string='Precio')

    import_id = fields.Many2one('stock.imports.history', string='Importaciones')

    arancel_id = fields.Many2one('stock.movement.arancel', string='Arancel aplicado')


    def calculate_arancel_final_price(self):
        for record in self:
            arancel_total_price = 0

            category_id = record.product_id.product_tmpl_id.categ_id
            arancel_id = self.env['stock.movement.arancel'].search([('category_id', '=', category_id.id)])
            record.arancel_id = arancel_id
            for arancel in arancel_id:
                arancel_total_price = record.price * record.quantity * (arancel.tasa / 100)

            total_price = arancel_total_price + record.price * record.quantity
            return total_price

