def format_price(price: int, discount: int = 30): # annotation for keyword variable 
    # annotation for a regular variable (price: int, name: str)
    # for a keyword variable (name: str = Dima)
    price = int(price)
    result = f"Price: {price} USD"
    return(result)

a = format_price(56.24)
print(a)