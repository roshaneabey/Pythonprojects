import pandas as pd
import sqlite3

#Extracting data
print("Extracting data from CSV...")

#Load the messy CSV File into a pandas dataframe
dataframe=pd.read_csv("messy_sales.csv")

#Transforming data
print("Cleaning Data...")

#Drop any row that is missing a value(eg: empty items or amount)
clean_df= dataframe.dropna()

print(f"Removed {len(dataframe)-len(clean_df)} invalid rows.")

#Loading processed data
print("Connecting to database...")

#Connect to a local SQlite database file(New file is created)
conn=sqlite3.connect("company_sales.db")

#Push the clean data into a SQL table named 'dailysales'
#if_exsists="append" meaning it will add new data without deleting old data

clean_df.to_sql("daily_sales",conn, if_exists="append",index=False)

print("Data successfully loaded into SQL")

#The code below makes the calulations for daily totals, execute it against our newly created database

print("\nDaily Sales Report\n")

#Standard SQL to group the sales by data and sum the amounts

query = """
    SELECT Date,SUM(Amount)as Total_Revenue
    FROM daily_sales
    GROUP BY Date
    """
#Run the query and store the results
report = pd.read_sql(query,conn)

#Print the final Report
print(report)

#Always close the database connection after using a database
conn.close()






