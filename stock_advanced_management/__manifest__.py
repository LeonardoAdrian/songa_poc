{
    'name': "Stock Advanced Management",
    'summary': "Modulo base para gestion de Exportaciones e Importaciones",
    'description': "Contiene el comportamiento base para la gestion de los procesos de exportacion e importacion de productos",
    'author': "Inti Soluciones",
    'website': "www.intisoluciones.com",
    'version': '0.1',
    'depends': ['stock', 'documents'],
    'data': [
        'views/stock_movement_arancel_view.xml',
        'views/stock_movement_fee_view.xml',
        'views/stock_transport_type_view.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/importacion-y-exportacion.png',
    ],
    'installable': True,
    'category': 'Inventario',
    'application': False,
    'assets': {
    },
}
