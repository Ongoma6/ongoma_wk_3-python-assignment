def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount= (discount_percent/100)*price
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
#Get User input for calculation
price = float(input("Enter Your original price for  the item: "))
discount_percent = float(input("Enter your percentages: "))

#Calculation of the final_price
final_price = calculate_discount(price, discount_percent)

#The Result for the calculation
if final_price< price:
    print(f"You got the discount, your final price is ${final_price}")
else:
    print(f"Unfortunality you do qualify for discount, your final price is ${price}") 
