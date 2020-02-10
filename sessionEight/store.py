def productName():
    name = input('Enter the product name').strip()
    if name:
        return name
    else:
        return productName()

def productQuantity():
    quantity = int(input('Enter the product quantity').strip())
    if quantity:
        return quantity
    else:
        return productQuantity()

def productPrice():
    price = int(input('Enter the product price').strip())
    if price:
        return price
    else:
        return productPrice()
product_list = []
add_more = 'y'
while add_more == 'y':
    name    = productName()
    quatity = productQuantity()
    price   = productPrice()
    import stock_inventory
    product = stock_inventory.addProduct(name,quatity,price)
    product_list.append(product)

    add_more = input(
            "\n\nDo you want add more products if yes then press 'y' else press any key: ")

stock_inventory.showProduct(product_list)
stock_inventory.removeProduct(product_list,'lays')
stock_inventory.showProduct(product_list)