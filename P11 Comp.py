# lb
print("...............Another Example...............")
input_name = input("Please Enter yor Name: ")
print(f'Hello {input_name}. Can i know your weight? ')
weight_type = input("Input your wight type first like 'kg' or 'lb' ? ")
user_weight_type_lb = "lb"
user_weight_type_kg = "kg"
user_weight = int(input("Enetr your Weight!"))
print(user_weight)
if weight_type == user_weight_type_lb:
    print(f'{input_name}, your weight in kg is = {user_weight*0.45}kg')
else:
    print(f'{input_name}, your weight in pound is = {user_weight/0.45 }lb')



