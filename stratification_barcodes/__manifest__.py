# Copyright 2019 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    'name': 'Stratification Barcodes',
    'version': '11.0.1.0.0',
    'summary': 'Stratification of Barcodes',
    'author': 'Eficent',
    'website': 'https://github.com/Eficent/user-group-segmentation',
    'license': 'LGPL-3',
    'depends': [
        'stratification_base',
        'barcodes',
    ],
    'data': [
        'data/module_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'sequence': 150,
    'installable': True,
    'application': False,
    'auto_install': False,
}
