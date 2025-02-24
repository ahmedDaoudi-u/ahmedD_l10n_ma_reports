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
        "data/moroccan_structure_type.xml",
        'reports/payslip_inheritance_report.xml',
        'data/paper_format_report.xml',
        'views/custom_employee_data.xml',
        "views/custom_time_off.xml",
        "data/moroccan_structure_rules.xml",
        "data/moroccan_rules_non_agricole.xml",
        "data/moroccan_category_data_non_agricole.xml",
        "data/moroccan_salary_rules_non_agricole.xml",
        "data/cron-droit.xml",
        "views/custom_contract_employee.xml",
        "views/company_custom_profile.xml",
        "data/calendrier_maroc.xml",
        "data/employment_type.xml",
        "views/res_config_settings_view.xml",
        "views/custum_employee_maroc.xml",
        "data/moroccan_rules_agricole.xml"
    ],
    "assets": {
        'web.report_assets_common' :
        ['teos_l10n_ma_reports/static/src/CSS/custom_page.css'],

    },
    "category": "",
    "depends": ['hr_payroll', 'l10n_ma', 'hr_holidays', 'base', 'hr_contract', 'l10n_ma_hr_payroll'],
    "installable": True,
    "application": True,
    "license": "LGPL-3"

}
