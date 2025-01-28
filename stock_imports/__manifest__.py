{
    'name': "Stock Imports",
    'icon': 'stock_imports/static/description/importacion-y-exportacion.png',
    'summary': "Modulo para gestion de Importaciones",
    'description': "Gestiona el proceso de importaciones de productos de inventario",
    'author': "Inti Soluciones",
    'website': "www.intisoluciones.com",
    'version': '0.1',
    'depends': ['stock', 'documents', 'stock_advanced_management', 'account'],
    'data': [
        'views/supplier_view.xml',
        'views/imports_view.xml',
        'views/import_line_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
    ],
    'installable': True,
    'category': 'Inventario',
    'application': True,
    'assets': {
    },
}
