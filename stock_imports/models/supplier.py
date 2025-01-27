from odoo import models, fields

from odoo import models, fields

class StockImportsSupplier(models.Model):
    _name = 'stock.imports.supplier'
    _description = 'Registro de Proveedores'

    # Información Básica
    name = fields.Char(string='Nombre del Proveedor', required=True)
    supplier_code = fields.Char(string='Código del Proveedor', required=True)
    supplier_type = fields.Selection(
        [('national', 'Nacional'), ('international', 'Internacional')],
        string='Tipo de Proveedor'
    )
    currency_id = fields.Many2one('res.currency', string='Moneda de Pago')

    phone = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    website = fields.Char(string='Página Web')

    # Información Financiera
    payment_journal_id = fields.Many2one(
        'account.journal',
        string='Metodos de pago',
    )
    bank_account_id = fields.Many2one(
        'res.partner.bank',
        string='Cuenta Bancaria',
    )
    payment_term_id = fields.Many2one(
        'account.payment.term',
        string='Términos de Pago'
    )
    credit_limit = fields.Float(string='Límite de Crédito')

    # Información Logística
    delivery_time = fields.Integer(string='Tiempo de Entrega Promedio (días)')
    delivery_terms = fields.Char(string='Términos de Entrega')
    delivery_address = fields.Text(string='Dirección de Entrega')

    # Información Adicional
    internal_notes = fields.Text(string='Notas Internas')



