from odoo import models, fields, api


class StockImportsHistory(models.Model):
    _name = 'stock.imports.history'
    _description = 'Historial de Importaciones'

    # Relación con el modelo de proveedores
    supplier_id = fields.Many2one(
        'stock.imports.supplier',
        string='Proveedor',
        required=True,
        ondelete='cascade'
    )
    # Campos del historial de importaciones
    import_date = fields.Date(string='Fecha de Importación', required=True, default=fields.Date.today())
    product_name = fields.Char(string='Producto Importado', required=True)
    quantity = fields.Float(string='Cantidad', required=True)
    import_cost = fields.Float(string='Costo de Importación', required=True)
    state = fields.Selection(
        [('draft', 'Borrador'), ('in_transit', 'En Tránsito'), ('received', 'Recibido'), ('cancelled', 'Cancelado')],
        string='Estado',
        default='draft'
    )
    notes = fields.Text(string='Notas')

    arancel_id = fields.Many2one(
        'stock.movement.arancel',  # Nombre del modelo de aranceles
        string='Arancel',
        domain="[('movement_type', '=', 'Importacion')]"  # Filtra solo aranceles de tipo 'importacion'
    )
    tarifa_id = fields.Many2one(
        'stock.movement.fee',  # Nombre del modelo de tarifas
        string='Tarifa',
        domain="[('movement_type', '=', 'Importacion')]"  # Filtra solo tarifas de tipo 'importacion'
    )

    # Campos calculados para costos
    costo_arancel = fields.Float(string='Costo de Arancel', compute='_compute_costos', store=True)
    costo_tarifa = fields.Float(string='Costo de Tarifa', compute='_compute_costos', store=True)
    costo_total = fields.Float(string='Costo Total', compute='_compute_costos', store=True)

    @api.depends('import_cost', 'arancel_id', 'tarifa_id')
    def _compute_costos(self):
        for record in self:
            # Calcular costo de arancel
            if record.arancel_id:
                record.costo_arancel = record.import_cost * (record.arancel_id.tasa / 100)
            else:
                record.costo_arancel = 0

            # Calcular costo de tarifa
            if record.tarifa_id:
                if record.tarifa_id.tipo_tarifa == 'fijo':
                    record.costo_tarifa = record.tarifa_id.costo
                else:
                    record.costo_tarifa = record.import_cost * (record.tarifa_id.costo / 100)
            else:
                record.costo_tarifa = 0

            # Calcular costo total
            record.costo_total = record.import_cost + record.costo_arancel + record.costo_tarifa