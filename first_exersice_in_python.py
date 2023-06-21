sales = []

while True:
    company_name = input("please enter your company name :")

    product_name = input("please center your product name :")

    quantity_sold = int(input("please enter the quantity sold :"))

    sales.append({"company": company_name, "product": product_name, "quantity": quantity_sold})

    another = input("do you want to add another ? (y/n)")

    if another != "y":
        break

total_sales = sum([sale["quantity"] for sale in sales])
print(sales)
print("Total Sales:", total_sales)
