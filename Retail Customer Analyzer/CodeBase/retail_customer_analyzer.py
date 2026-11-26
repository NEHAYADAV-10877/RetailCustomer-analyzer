# Retail Customer Analyzer
# Beginner-friendly project using Python and Pandas

import pandas as pd

# Step 1: Load the CSV file
try:
    customers = pd.read_csv("customers.csv")
except FileNotFoundError:
    print("Error: customers.csv file not found. Keep it in the same folder as this program.")
    raise SystemExit

# Step 2: Show the menu repeatedly until the user exits
while True:
    print("\n===== RETAIL CUSTOMER ANALYZER =====")
    print("1. Spending statistics")
    print("2. High-value customers")
    print("3. City-wise summary")
    print("4. Exit")

    choice = input("Enter your choice: ").strip()

    # Option 1: Calculate spending statistics
    if choice == "1":
        mean_spend = customers["TotalSpent"].mean()
        median_spend = customers["TotalSpent"].median()
        highest_customer = customers.loc[customers["TotalSpent"].idxmax()]
        lowest_customer = customers.loc[customers["TotalSpent"].idxmin()]

        print(f"Mean spend: Rs. {mean_spend:.2f}")
        print(f"Median spend: Rs. {median_spend:.2f}")
        print(f"Highest: {highest_customer['Name']} (Rs. {highest_customer['TotalSpent']:.0f})")
        print(f"Lowest: {lowest_customer['Name']} (Rs. {lowest_customer['TotalSpent']:.0f})")

    # Option 2: Find customers spending at least the given limit
    elif choice == "2":
        limit_text = input("Enter spending limit: ")

        try:
            limit = float(limit_text)
            if limit < 0:
                print("Amount must be 0 or more.")
            else:
                high_value = customers[customers["TotalSpent"] >= limit]
                print(f"High-value customers (TotalSpent >= {limit:g}): {len(high_value)}")

                if high_value.empty:
                    print("No customers found.")
                else:
                    for _, customer in high_value.iterrows():
                        print(f"{customer['CustomerID']} | {customer['Name']} | {customer['City']} | Rs. {customer['TotalSpent']:.0f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # Option 3: Group customer spending by city
    elif choice == "3":
        city_summary = customers.groupby("City")["TotalSpent"].agg(["sum", "mean"])
        print("City-wise summary:")
        for city, values in city_summary.iterrows():
            print(f"{city} : Total Rs. {values['sum']:.0f} | Average Rs. {values['mean']:.2f}")

    # Option 4: Stop the program
    elif choice == "4":
        print("Thank you for using Retail Customer Analyzer!")
        break

    # Handle menu choices other than 1, 2, 3 or 4
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")
