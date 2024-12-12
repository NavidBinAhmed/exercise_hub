'''# function definition

def total_cost_calculator(cart):
    total_cost = 0

    for item in cart:
        total_cost += item['price'] * item['quantity']
    
    return total_cost


# stored carts: driver code
cart = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 4},
    {'name': 'Banana', 'price': 0.3, 'quantity': 8},
    {'name': 'Orange', 'price': 0.6, 'quantity': 10}
]

# function calling
total_cost = total_cost_calculator(cart)
print('$',total_cost)'''



'''The following function will calculate the total cost of the cart'''
# function definition
'''def total_cost_calculator(cart):
    total_cost = 0

    for items in cart:
        total_cost = items['price'] * items['quantity']
    return total_cost


# example cart: driver code
cart = [
    {'name':'Apple', 'price': 5, 'quantity': 5},
    {'name':'Orange', 'price': 7, 'quantity': 4},
    {'name':'Banana', 'price': 6, 'quantity': 15},
    {'name':'Guava', 'price': 5, 'quantity': 10},
    {'name':'Grape', 'price': 9, 'quantity': 25}
]


# function calling
cost = total_cost_calculator(cart)
print("The total cost is US$", cost)

# output: The total cost is US$ 225'''





