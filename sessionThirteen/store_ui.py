import stock_inventory as si
import log_file

def show_menu():
    print("\n-----------------------------------------------")
    print("Code Girls - Store")
    print("-----------------------------------------------")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Show Products")
    print("4. Rename Product")
    print("5. Change Price")
    print("6. Increase Quantity")
    print("7. Decrease Quantity")
    print("8. Exit to store")
    print("9. Load Products")
    print("10.Save Products")
    print("\nFor selecting any option press number")

def take_select_option():
    user_input = int(input("Select option: "))
    print("\n")
    return user_input
try:
    opt = ""
    while opt != "8":
        if opt.strip() == "":
            pass
        elif opt.strip() == "1":
            si.take_add_product_input()
        elif opt.strip() == "2":
            si.take_remove_product_input()
        elif opt.strip() == "3":
            si.showProducts()
        elif opt.strip() == "4":
            si.take_rename_product_input()
        elif opt.strip() == "5":
            si.take_change_price_input()
        elif opt.strip() == "6":
            si.take_inc_qty_input()
        elif opt.strip() == "7":
            si.take_dec_qty_input()
        elif opt.strip() == "9":
            si.loadProduct()
        elif opt.strip() == "10":
            si.saveProduct()
        else:
            print("Wrong choice, Please select option from provided list.")

        show_menu()
        opt = take_select_option()
except Exception as e:
    log_file.log_errors(e)