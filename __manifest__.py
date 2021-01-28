# -*- coding: utf-8 -*-
{
    'name': "Contratos Empleados",
    'summary': """
           Generacion del contrato para los empleados PDF
        """,
    'author': "Ariel Cerrato",
    'website': "https://www.guip.com/",
    'category': 'Human Resources',
    'version': '1.0',
    'license': 'OPL-1',
    'data': [
        "reports/facturas_print.xml",
        "reports/facturas_print_view.xml",
        "reports/convenio_print .xml",
        "reports/convenio_print_view .xml",
        "views/contrato_add.xml",
    ],
    'depends': ['hr_contract'],
    'installable': True,
    'auto_install': False,
    'application': True,
}