import pandas as pd



data = [
    {
        "paymentId": 9001,
        "date": "2026-02-01",
        "tenant": {
            "tenantId": "T101",
            "name": "Abhi",
            "city": "Delhi"
        },
        "property": {
            "propertyId": "P501",
            "propertyName": "Greystar Heights",
            "unit": "A-101"
        },
        "charges": [
            {"type": "Rent", "amount": 18000},
            {"type": "Maintenance", "amount": 2000}
        ],
        "payment": {
            "method": "UPI",
            "status": "Success"
        }
    },
    {
        "paymentId": 9002,
        "date": "2026-02-01",
        "tenant": {
            "tenantId": "T102",
            "name": "Rahul",
            "city": "Mumbai"
        },
        "property": {
            "propertyId": "P502",
            "propertyName": "Greystar Residency",
            "unit": "B-202"
        },
        "charges": [
            {"type": "Rent", "amount": 22000},
            {"type": "Parking", "amount": 1000}
        ],
        "payment": {
            "method": "Card",
            "status": "Success"
        }
    },
    {
        "paymentId": 9003,
        "date": "2026-02-02",
        "tenant": {
            "tenantId": "T103",
            "name": "Neha",
            "city": "Delhi"
        },
        "property": {
            "propertyId": "P501",
            "propertyName": "Greystar Heights",
            "unit": "A-105"
        },
        "charges": [
            {"type": "Rent", "amount": 18000},
            {"type": "Maintenance", "amount": 2000}
        ],
        "payment": {
            "method": "UPI",
            "status": "Failed"
        }
    }
]

df = pd.json_normalize(
    data,
    record_path="charges",
    meta=[
        "paymentId",
        "date",
        ["tenant", "tenantId"],
        ["tenant", "name"],
        ["tenant", "city"],
        ["property", "propertyId"],
        ["property", "propertyName"],
        ["property", "unit"],
        ["payment", "method"],
        ["payment", "status"]
    ]
)

df.columns = [
    "chargeType", "amount",
    "paymentId", "date",
    "tenantId", "tenantName", "tenantCity",
    "propertyId", "propertyName", "unit",
    "paymentMethod", "paymentStatus"
]

print(df)

# Successful payments filter karo
df_success = df[df["paymentStatus"] == "Success"]
print("\n Successful payments made:\n", df_success)


# df_success mein saaari successful paymentStatus vala data feed hogya hai (not FAILED) so all the below operations are performed on successful payments:

# Successful payment me se specific paymentId
row = df_success[df_success["paymentId"] == 9002]
print(row)

# Successful payment me se tenant wise
row = df_success[df_success["tenantName"] == "Abhi"]
print(row)

# Successful payment me se first row only
row = df_success.head(1)
print(row)

# Successful payment me se property wise
row = df_success[df_success["propertyName"] == "Greystar Heights"]
print(row)


# Total Revenue calculate karo
total_revenue = df_success["amount"].sum()
print("\nTOTAL REVENUE (SUCCESS):", total_revenue)

# ChargeType wise revenue
charge_type_wise_revenue = df_success.groupby("chargeType")["amount"].sum()
print("\nCHARGE TYPE WISE REVENUE:\n", charge_type_wise_revenue)

# Property wise revenue
property_wise_revenue = df_success.groupby("propertyName")["amount"].sum()
print("\n PROPERTY WISE REVENUE:\n", property_wise_revenue)

 # Tenant wise Total Paid
tenant_wise_revenue = df_success.groupby("tenantId")["amount"].sum()
print("\n TENANT WISE TOTAL PAID:\n", tenant_wise_revenue)

# Failed Payments Report
df_failed = df[df["paymentStatus"] == "Failed"]
print("\n FAILED PAYMENTS REPORT:\n", df_failed)

# Outstanding Amount (Failed payments sum)
outstanding_amount = df_failed["amount"].sum()
print("\nTOTAL OUTSTANDING (FAILED):", outstanding_amount)

# Tenant Outstanding Report
from tabulate import tabulate

tenant_due = df_failed.groupby("tenantName")["amount"].sum().reset_index()
tenant_due.columns = ["tenantName","outstanding_amount"]
print("\nTENANT DUE REPORT:\n")
print(tabulate(tenant_due, headers="keys", tablefmt="grid", showindex=False))

# Property Outstanding Report
property_due = df_failed.groupby("propertyName")["amount"].sum().reset_index()
property_due.columns = ["propertyName", "dueAmount"]

print("\nPROPERTY DUE REPORT:\n")
print(tabulate(property_due, headers="keys", tablefmt="grid", showindex=False))


# Export all reports to CSV (Power BI ready) 
df_success.to_csv("successful_payment.csv", index=False)
df_failed.to_csv("failed_payments.csv", index=False)
charge_type_wise_revenue.to_csv("charge_type_wise_revenue.csv", index=False)
property_wise_revenue.to_csv("property_wise_revenue.csv", index=False)
tenant_wise_revenue.to_csv("tenant_wise_revenue.csv", index=False)

print("\nAll reports exported as CSV files.")

# Ab hum Power BI / Tableau ready final master dataset banayenge jisme:

# TotalPaid (success)

# TotalDue (failed)

# Tenant wise summary

# Property wise summary


# Tenant Summary Table (Paid + Due)
paid_summary = df_success.groupby("tenantId")["amount"].sum().reset_index()
paid_summary.columns = ["tenantId","totalPaid"]

due_summary = df_failed.groupby("tenantId")["amount"].sum().reset_index()
due_summary.columns = ["tenantId","totalDue"]

# fillna(0) -> pandas library to replace all missing (NaN or Null) values in a DataFrame or Series with the value 0
tenant_summary = pd.merge(paid_summary, due_summary, on = "tenantId", how = "outer").fillna(0) 

print("\nTENANT SUMMARY REPORT:\n")
print(tabulate(tenant_summary, headers="keys", tablefmt="grid", showindex=False))

tenant_summary.to_csv("tenant_summary.csv", index=False)
print("\nExported: tenant_summary.csv")

# Property Summary Table (Paid + Due)
paid_property = df_success.groupby("propertyName")["amount"].sum().reset_index()
paid_property.columns = ["propertyName", "totalPaid"]

due_property = df_failed.groupby("propertyName")["amount"].sum().reset_index()
due_property.columns = ["propertyName", "totalDue"]

property_summary = pd.merge(paid_property, due_property, on="propertyName", how="outer").fillna(0)

print("\nPROPERTY SUMMARY REPORT:\n")
print(tabulate(property_summary, headers="keys", tablefmt="grid", showindex=False))

property_summary.to_csv("property_summary.csv", index=False)
print("\nExported: property_summary.csv")
