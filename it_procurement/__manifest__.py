# -*- coding: utf-8 -*-
{
    "name": "IT Procurement",
    "summary": "IT Procurement Application",
    "description": """
        IT Procurement
    """,
    "author": "Mohiuddin",
    "website": "mohiuddinru.github.io",
    "category": "Purchases",
    "version": "0.0.1",
    "depends": ["base", "purchase"],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "security/purchase_order_rules.xml",
        "views/views.xml",
        "views/templates.xml",
    ],
    "demo": [
        # 'demo/demo.xml',
    ],
}
