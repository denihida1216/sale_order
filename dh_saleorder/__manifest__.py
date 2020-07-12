# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'DH - Sale Order Custom Set Confirm All & Partner Show By Salesperson',
    'version': "10.0.1.1",
    'category': 'Sales',
    'description': """
    Set Confirm All, Partner Show By Salesperson
    """,
    'summary': 'Sales Custom For Odoo 10',
    'sequence': '10',
    'author': 'Deni Hidayat',
    'company': 'Deni Hidayat',
    'maintainer': 'Deni Hidayat',
    'support': 'denihida1216@gmail.com',
    'website': 'https://denihida1216.github.io',
    'depends': [
        'base',
        'web',
        'product',
        'stock',
        'sale',
        'account'
    ],
    'demo': [],
    'data': [
        'security/sale_security.xml',
        'views/stock_warehouse_view.xml',
        'views/wizard_sale_order_view.xml',
    ],
    'license': "AGPL-3",
    "images": [
        "static/description/images/odoo4.png",
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}
