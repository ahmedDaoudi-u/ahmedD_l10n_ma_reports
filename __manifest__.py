{
    "name": "Teos - Accounting Report",
    "version": "17.0.1.0.0",
    "website": "https://www.report.com",
    "summary": "Accounting reports for Teos",
    'category': 'Customizations/Custom',
    "author": "Ahmed",
    "description": "This Is A Project For Payslip Reporting",
    "data": [
        'security/ir.model.access.csv',
        'reports/payslip_inheritance_report.xml',
        'data/paper_format_report.xml'
    ],
    "category": "",
    "depends": ['l10n_ma_hr_payroll','hr_payroll', 'l10n_ma'],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}
