import pandas as pd

# Original DataFrame from the earlier stages
risk_data = {
    "Asset": [
        "RetailSuite CRM",
        "E-Shop Plus",
        "Insight Analytics",
        "Cloud Database (PostgreSQL)",
        "Internal Employee Systems (HR, Payroll)",
        "ABC Mobile App",
        "Employee VPN Access",
        "Corporate Email System (Office 365)",
        "Cloud-Based Customer Support System (Zendesk)",
        "Internal File Sharing System (SharePoint)",
        "Cloud Backup System (Azure)",
        "Internal Payroll System (QuickBooks Online)",
        "Supply Chain Management System",
        "Business Intelligence Dashboard (Power BI)",
        "Public-Facing Website (WordPress)"
    ],
    "Risk Treatment": [
        "Patch SQL Injection and enhance input sanitization",
        "Update XSS prevention and input validation",
        "Secure API endpoints with authentication and encryption",
        "Upgrade PostgreSQL to the latest version",
        "Implement password policies and employee training",
        "Enhance API encryption and replace PIN with biometric/multi-factor",
        "Update VPN encryption and enforce unique credentials",
        "Upgrade phishing filters and enforce email encryption",
        "Implement RBAC and redact sensitive data in tickets",
        "Audit and restrict SharePoint permissions, enforce encryption",
        "Regularly verify backup integrity and limit access controls",
        "Deactivate inactive accounts and apply patches",
        "Remove hardcoded credentials and patch vulnerabilities",
        "Implement strong password policies and MFA",
        "Update plugins and deploy DDoS protection"
    ],
    "Estimated Cost ($)": [
        5000, 4000, 6000, 4500, 2000, 5500, 3000, 2500, 4000, 3500, 5000, 3000, 4000, 2500, 2000
    ],
    "Priority": [
        "High", "High", "High", "High", "Medium", "High", "Medium", "Medium", "Medium", "Medium", 
        "Medium", "Medium", "Medium", "Low", "Medium"
    ],
    "Planned Date": [
        "2024-11-10", "2024-11-12", "2024-11-15", "2024-11-17", "2024-11-20", "2024-11-25",
        "2024-11-22", "2024-11-18", "2024-11-28", "2024-11-27", "2024-11-30", "2024-11-29",
        "2024-12-02", "2024-12-05", "2024-12-10"
    ],
    "Implementation Date": [
        "2024-12-01", "2024-12-03", "2024-12-07", "2024-12-08", "2024-12-15", "2024-12-10",
        "2024-12-20", "2024-12-12", "2024-12-18", "2024-12-17", "2024-12-25", "2024-12-22",
        "2024-12-28", "2024-12-30", "2025-01-05"
    ]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(risk_data)

# Save to an Excel file
file_path = "/mnt/data/Risk_Assessment_With_Treatment.xlsx"
df.to_excel(file_path, index=False)

file_path
