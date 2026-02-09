# Tenant-Payment-Analytics 🏢💳  
### Power BI Dashboard + Python Data Processing Project

Tenant-Payment-Analytics is an end-to-end analytics project where tenant rent payment data is created using Python (Pandas), exported into structured CSV reports, and visualized using an interactive Power BI dashboard.

This project analyzes:
- Total rent collected vs pending dues
- Failed payment transactions
- Property-wise and tenant-wise payment performance
- Charge type revenue breakdown (Rent, Maintenance, Parking)

---

## 📌 Project Overview

This project simulates a real-world **Rent Collection & Payment Monitoring System**.

A dummy/synthetic dataset is generated in Python, cleaned and transformed using Pandas, and then exported into Power BI-ready CSV files.  
These datasets are imported into Power BI to build an interactive dashboard for rent payment tracking.

---

## 🛠 Tech Stack

- **Python**
  - pandas
  - requests
  - tabulate
- **Power BI Desktop**
- **CSV / Excel Reports**

---

## 📂 Project Structure

```txt
Tenant-Payment-Analytics/
│
├── api_analysis.py
├── greystar_analysis.py
│
├── tenant_overview.pbix
│
├── successful_payment.csv
├── failed_payments.csv
├── tenant_summary.csv
├── property_summary.csv
├── tenant_wise_revenue.csv
├── property_wise_revenue.csv
├── charge_type_wise_revenue.csv
│
└── final_users_data.csv
```
## 📊 Generated CSV Reports

The Python script generates the following Power BI-ready reports:

### ✅ Payment Reports
- `successful_payment.csv` → Successful rent transactions  
- `failed_payments.csv` → Failed transactions (outstanding dues)

### ✅ Summary Reports
- `tenant_summary.csv` → Tenant-wise total paid and total due  
- `property_summary.csv` → Property-wise total paid and total due  

### ✅ Revenue Reports
- `tenant_wise_revenue.csv` → Tenant-wise revenue collected  
- `property_wise_revenue.csv` → Property-wise revenue collected  
- `charge_type_wise_revenue.csv` → Charge type revenue breakdown (Rent/Maintenance/Parking)

---

## 📈 Power BI Dashboard Pages

### ✅ Overview Dashboard
- Total Properties  
- Total Tenants  
- Total Paid Amount  
- Total Due Amount  
- Collection Rate %  
- Rent vs Other Charges  
- Property-wise Paid Amount  
- Property-wise Due Amount  
- Charge Type Wise Revenue Segregation  

### ❌ Failed Payments Page
- Failed Transactions Count  
- Tenant-wise outstanding amount  
- Property-wise due distribution

## 🧮 DAX Measures Used

```DAX
Total Paid = SUM(successful_payment[amount])

Total Due = SUM(failed_payments[amount])

Failed Transactions = DISTINCTCOUNT(failed_payments[paymentId])

Collection Rate % = 
DIVIDE([Total Paid], [Total Paid] + [Total Due], 0)

Delinquency Rate % = 
DIVIDE([Total Due], [Total Paid] + [Total Due], 0)
```

## 🚀 How to Run the Project

### Step 1: Run Python Script  
Generate all CSV reports:

python greystar_analysis.py  

(Optional API practice script)

python api_analysis.py  

---

### Step 2: Open Power BI Dashboard  
Open the Power BI file:

tenant_overview.pbix  

Then click:

✅ Refresh Data  
to load the latest generated CSV datasets.

---

## 📸 Dashboard Preview

Add your Power BI dashboard screenshot inside an images/ folder and use this:

![Dashboard Preview](images/dashboard.png)

---

## 🔍 Key Insights Delivered

- Comparison of Total Paid vs Total Due  
- Monitoring of Collection Rate %  
- Identification of Failed Transactions  
- Tenant-wise payment performance tracking  
- Property-wise rent collection comparison  
- Charge type revenue breakdown (Rent, Maintenance, Parking)  

---

## 📌 Future Enhancements

- Month-wise rent collection trend analysis  
- Tenant delinquency ranking system  
- Predictive due forecasting  
- SQL database integration instead of CSV files  

---

## 👤 Author

Abhinandan (Abhi)
