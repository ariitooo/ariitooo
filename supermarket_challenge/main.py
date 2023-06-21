store_list = []
customer_list = []
purchases = []
shopping_list = []

def show_menu():
    print('''
    1) Add Product (Panel For Seller)
    2) Add Customer
    3) Show All Products
    4) Show All Customers
    5) Shopping
    6) Show All Shoppings
    7) Search By Product code
    8) Search by customer Name
    0) Exit
    ''')
    return int(input("choice your operation : "))


def add_product():
    store = {
        "product_code": int(input("Enter product`s code : ")),
        "product_name": input("Enter product`s name : "),
        "product_price": input("Enter product`s price : "),
        "product_discount": input("Enter product`s discount : "),
        "product_count": input("Enter product`s count : ")
    }

    store_list.append(store)
    print("Product Saved")


def add_customer():
    customer = {
        "customer_code": int(input("Enter customer`s code : ")),
        "customer_name": input("Enter customer`s name : "),
        "customer_family": input("Enter customer`s family : ")
    }

    customer_list.append(customer)
    print("Your Customer Saved")


def shopping():
    shop = {}
    print_all_customers()
    customer_code = int(input("Enter Customer Code : "))

    for c in customer_list:
        if c["customer_code"]==customer_code:
            shop["customer"] = c
            break


    print_all_products()

    product_list = []

    while input("Select Product (y/n) ? ") == "y":
        product_code = int(input("Enter Product Code : "))
        count = int(input("Enter Count : "))
        for p in store_list:
            if p["product_code"] == product_code:
                if p["product_count"] <= count:
                    product_list.append(p)
                else:
                    print("Count is not available")
                break


    shop["product_list"] = product_list
    shopping_list.append(shop)
    print("Shopping Saved")



def totally_all():
    while True:
        for i in range(len(store_list)):

            if store_list[i]["product_code"] == customer_list[i]["product_code"]:

                discount = int(store_list[i]["product_discount"]) / 100

                purches_price = int(store_list[i]["product_price"]) * int(customer_list[i]["count"]) * (1 - discount)

                purchase = {"name": customer_list[i]["customer_name"],
                            "totall": purches_price
                            }

                purchases.append(purchase)
                print("$$$", purches_price, "$$$")
                show_menu()

            else:

                print("We did not find the product you selected...Try Again !")
                exit()


def print_total_shopping():
    for shop in shopping_list:
        print(shop["customer"])
        for product in shop["product_list"]:
            print("\t", product)


def print_all_products():
    for product in store_list:
        if product["product_count"] > 0:
            print(product)


def print_all_customers():
    for customer in customer_list:
        print(customer)


def find_by_product_code():
    search_p_c = input("Seach by Product Cod : ")

    for i in store_list:

        if i == search_p_c:

            print(i, "Found")

        else:

            print("Not Found")


def find_by_customer_name():
    search_c_n = input("Search by Customer Name : ")

    for i in customer_list:

        if i == search_c_n:

            print("Found")

        else:

            print("Not Found")
