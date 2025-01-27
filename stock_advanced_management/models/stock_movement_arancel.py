from odoo import models, fields

class StockImportsArancel(models.Model):
    _name = 'stock.movement.arancel'
    _description = 'Aranceles'

    name = fields.Char(string='Nombre del Arancel', required=True)
    tasa = fields.Float(string='Tasa (%)', required=True, help="Porcentaje de la tasa de arancel.")
    fecha_vigencia = fields.Date(string='Fecha de Vigencia', required=True, default=fields.Date.today())
    active = fields.Boolean(string='Activo', default=True)
    movement_type = fields.Selection([
        ('exportacion', 'Exportacion'),
        ('importacion', 'Importacion'),
    ], string='Show status')