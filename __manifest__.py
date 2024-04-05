{
    "name": "Teos - Accounting Report",
    "version": "17.0.1.0.0",
    'countries': ['ma'],
    "website": "https://www.report.com",
    "summary": "Accounting reports for Teos",
    'category': 'Customizations/Custom',
    "author": "Ahmed",
    "description": "This Is A Project For Payslip Reporting",
    "data": [
        'security/ir.model.access.csv',
        'reports/payslip_inheritance_report.xml',
        'data/paper_format_report.xml',
        'views/custom_employee_data.xml',
        "views/custom_time_off.xml",
        "data/moroccan_structure_rules.xml",
        "data/moroccan_rules.xml",
        "data/moroccan_category_data.xml",
        "data/moroccan_structure_type.xml",
        "data/moroccan_salary_rules.xml",
    ],
    "category": "",
    "depends": ['l10n_ma_hr_payroll','hr_payroll', 'l10n_ma','hr_holidays'],
    "installable": True,
    "application": True,
    "license": "LGPL-3"

}
