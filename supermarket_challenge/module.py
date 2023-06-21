from main import *

while True:
    op = show_menu()
    print("*" * 60)

    if op == 1:
        add_product()

    elif op == 2:
        add_customer()

    elif op == 3:
        print_all_products()

    elif op == 4:
        print_all_customers()

    elif op == 5:
        shopping()

    elif op == 6:
        print_total_shopping()

    elif op == 7:
        find_by_product_cod()

    elif op == 8:
        find_by_customer_name()
    elif op == 0:
        exit()
    else:
        print("Invalid Option")

    print("*" * 60)