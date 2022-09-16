# -*- coding: utf-8 -*-
{
    'name': "Emplois_Fsegt",
    'summary': "Emplois_Fsegt",
    'description': "Emplois du temps",
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'author': "My Company",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'price': '20.0',
    'category': 'Emplois',
    'version': '15.0.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/contactbi_view.xml',
        'views/salles_view.xml',
        'views/matiéres_view.xml',
        'views/cellule_view.xml',
        'views/lundi_view.xml',
        'views/mardi_view.xml',
        'views/merecredi_view.xml',
        'views/jeudi_view.xml',
        'views/vendredi_view.xml',
        'views/samedi_view.xml',
        'views/groupes_view.xml',
        'views/test-view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
}
