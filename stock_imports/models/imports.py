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
    import_lines_ids = fields.One2many(
        comodel_name='stock.import.line',
        inverse_name='import_id',
        string='Productos a importar',
    )

    transport_type = fields.Many2one('stock.transport.type', string='Tipo de transporte')
    distance = fields.Float(string='Distancia (km)')
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
    costo_arancel = fields.Float(string='Costo de Arancel')
    costo_tarifa = fields.Float(string='Costo de Tarifa')
    costo_total = fields.Float(string='Costo Total')
    @api.onchange('distance','transport_type')
    def _compute_tarifa(self):
        for record in self:
            record.costo_tarifa = record.distance * record.transport_type.transport_fee


    @api.onchange('import_lines_ids')
    def _compute_costos(self):
        for record in self:

            total_cost_without_trasnport_fee = 0

            for line in record.import_lines_ids:
                total_cost_without_trasnport_fee += line.calculate_arancel_final_price()
            record.costo_arancel = total_cost_without_trasnport_fee
            transport_fee = record.distance * record.transport_type.transport_fee

            record.costo_total = transport_fee + total_cost_without_trasnport_fee
