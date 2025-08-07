# This is where all modules are published

> [!warning]
> Remember that all directories defined in odoo.conf as addons path must exist and cannot be empty; otherwise, Odoo services will crash and not start.

```configurations
addons_path = /mnt/extra-addons/oca,                                OCA Modules
              /mnt/extra-addons/pro,                                Third-party private and public Modules
              /mnt/extra-addons/dev,                                My own modules
              /mnt/extra-addons/test                                Third-party modules in testing but not included yet in the project
```

## Base modules for Medinec

| No | Name                       | Summary                                                                                      |
|----|----------------------------|----------------------------------------------------------------------------------------------|
| 1  | muk_web_dialog             | Adds options for the dialogs                                                                 |
| 2  | muk_web_colors             | Customize your Odoo colors                                                                   |
| 3  | muk_web_theme              | Odoo Community Backend Theme                                                                 |
| 4  | muk_web_appsbar            | Adds a sidebar to the main screen                                                            |
| 5  | muk_web_chatter            | Adds options for the chatter                                                                 |
| 6  | om_account_accountant      | Accounting Reports, Asset Management and Budget, Recurring Payments, Lock Dates, Fiscal Year, Accounting Dashboard, Financial Reports, Customer Follow up Management, Bank Statement Import |
| 7  | om_account_followup        | Customer FollowUp Management                                                                 |
| 8  | accounting_pdf_reports     | Accounting Reports For Odoo 17                                                               |
| 9  | om_recurring_payments      | Use recurring payments to handle periodically repeated payments                              |
| 10 | om_account_daily_reports   | Cash Book, Day Book and Bank Book Report For Odoo 17                                         |
| 11 | om_account_budget          | Odoo 17 Budget Management                                                                    |
| 12 | om_fiscal_year             | Odoo 17 Fiscal Year, Fiscal Year in Odoo 17, Lock Date in Odoo 17                            |
| 13 | om_account_asset           | Odoo 17 Assets Management                                                                    |
| 14 | session_db                 | No summary found                                                                             |
| 15 | stock_analytic             | Adds analytic distribution in stock move                                                     |
| 16 | l10n_ec_account_edi        | Electronic data interchange adapted Ecuadorian localization                                  |
| 17 | l10n_ec_withhold           | Electronic Withholding adapted Ecuadorian localization                                       |
| 18 | l10n_ec_base               | Ecuadorian Localization                                                                      |
| 19 | l10n_ec_credit_note        | No summary found                                                                             |
