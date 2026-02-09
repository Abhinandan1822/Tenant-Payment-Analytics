import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

# Flatten JSON
df = pd.json_normalize(data)

print(df.head())
print("\nTotal Columns:", len(df.columns))
print("\nColumns:\n", df.columns)

# Task: City-wise count (kitne users kis city se hain)
city_count = df["address.city"].value_counts()
print("\n City wise users Count:\n",city_count)

# Task: Company-wise count (kitne users kis company se hain)
company_count = df["company.name"]. value_counts()
print("\n Company wise users count:\n",company_count)

top_company = df["company.name"].value_counts().idxmax()
print("\n Top Company:", top_company)

# Goal: kis domain ke emails zyada hain (biz, org, net, info etc.)
df["email_domain"] = df["email"].str.split("@").str[1]

domain_count = df["email_domain"].value_counts()

print("\nEmail Domain Count:\n", domain_count)

# Final Clean Table export (CSV)
final_df = df[[
    "id",
    "name",
    "username",
    "email",
    "email_domain",
    "address.city",
    "address.zipcode",
    "company.name",
    "website"
]]

print("\nFinal Dataset Preview:\n", final_df.head())

final_df.to_csv("final_users_data.csv", index=False)
print("\nCSV file exported: final_users_data.csv")
