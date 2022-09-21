number_of_apples = int(input("How many apples do you have? "))
calculation_type = input("Select calculation unit? Type k for KG or l for lbs: ")

weight_in_kilogram = number_of_apples / 5
kg_to_lbs_coefficient = 2.20462

if calculation_type == 'k':
    print(f"Weight of apples {weight_in_kilogram} kg")
elif calculation_type == 'l':
    print(f"Weight of apples {weight_in_kilogram * kg_to_lbs_coefficient} lbs")    
else:
    print("Unknown option")
