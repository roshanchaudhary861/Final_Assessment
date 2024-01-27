price_of_pizza = 12
delivery_cost = 2.50
discount_on_Tuesday = 0.50
app_discount = 0.25

# defining function to calculate total cost of order
def calculate_total_cost(number_of_pizzas, is_tuesday, is_delivery, is_BPP_app,):
 
    if is_tuesday:
        pizza_price = price_of_pizza * discount_on_Tuesday
    else:
        pizza_price = price_of_pizza
        
    
    if is_delivery and number_of_pizzas < 5:  
        delivery_cost = 2.50
    else:
        delivery_cost = 0
    total_with_delivery = (number_of_pizzas * pizza_price) + delivery_cost   
 

    if is_BPP_app: 
        total_price = total_with_delivery * (1 - app_discount)
    else:
        total_price = total_with_delivery
    return total_price
    

def is_valid_integer(string):
    try:
        value = int(string)
        if value < 0:
            print(" Please enter a positive integer!")
            return False
        return True
    except ValueError:
        print(" Please enter a number!")
        return False
    
        
    


# Initialize a variable to store the number of pizzas
number_of_pizzas = None
print("```text\n","BPP Pizza Price Calculator\n","=" * 26,"\n") 

# Loop until the user enters a valid integer
while number_of_pizzas is None:
  
  user_input = input(" How many pizzas ordered? ")
  if is_valid_integer(user_input):
    number_of_pizzas = int(user_input)

            
# defining function to get yes or no input from user
def shouldContinue(prompt="Do you wish to continue?", answe='yes', answer='no'):
    while True:
        answer = input(prompt)
        if answer == 'y'.upper():
            return True
        elif answer == 'n'.upper():
            return False
        else:
            print(' please answer "Y" or "N".')
        continue
is_delivery = shouldContinue(" Is delivery required? ") 
is_tuesday = shouldContinue(" Is it Tuesday? ") 
is_BPP_app = shouldContinue(" Did the customer use the app? ") 

total_price = calculate_total_cost(number_of_pizzas, is_tuesday, is_delivery, is_BPP_app,)

print ("\nTotal Price: £","{:.2f}".format(total_price), end=".\n" )
print("```")

