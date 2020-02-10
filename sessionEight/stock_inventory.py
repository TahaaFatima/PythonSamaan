def addProduct(name,quatity,price):
    product_dict = {'product_name' : name, 'product_quantity' : quatity, 'product_price' : price}

    return product_dict

def showProduct(product_list):
    print(f"{'Product Name':<10} | {'Product Quantity':<5} | {'Product Price':<8}")
    for product_info in product_list:
        print(f"{product_info['product_name']:<10} | {product_info['product_quantity']:<5} | {product_info['product_price']:<8}")

def removeProduct(product_list,name):
    for product in product_list:
        if product['product_name'] == name:
            product.remove(product)
            break

