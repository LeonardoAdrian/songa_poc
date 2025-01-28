{
    'name': "Stock Exports",
    'icon': 'stock_exports/static/description/exporting.png',
    'summary': "Modulo para gestion de Exportaciones",
    'description': "Gestiona el proceso de exportaciones de productos de inventario",
    'author': "Inti Soluciones",
    'website': "www.intisoluciones.com",
    'version': '0.1',
    'depends': ['stock', 'documents', 'stock_advanced_management'],
    'data': [
        'views/custom_actions.xml',
        'views/stock_export_line_view.xml',
        'views/stock_export_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',

    ],
    'images': [
        'static/description/exporting.png'
    ],
    'installable': True,
    'category': 'Inventario',
    'application': True,
    'assets': {
    },
}
