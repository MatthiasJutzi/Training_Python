# Build an Apply Discount Function
# Try 1
# def apply_discount(price,discount):
#     if price != int or price != float:
#         return "The price should be a number"
#     elif discount != int or discount != float:
#         return "The discount should be a number"
#     elif price <= 0 
#         return "The price should be greater than 0"
#     elif discount < 0 or discount > 100:
#        return "The discount should be between 0 and 100"
#     else : 
#         discount_price = price - (price * discount / 100)
#         return discount_price
    
# price = int(input("Enter the price: "))
# discount = int(input("Enter the discount percentage: ")) 
# apply_discount(price,discount)


# try 2
# isinstance() in python is a built-in function that checks if an object is an instance of a specified class or a tuple of classes. 
# It returns True if the object is an instance of the class or any subclass thereof, and False otherwise.

def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    elif not isinstance(discount, (int, float)):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    else:
        discount_price = price - (price * (discount / 100))
        return discount_price

price = float(input("Enter the price: "))
discount = float(input("Enter the discount percentage: "))
print(apply_discount(price, discount))
