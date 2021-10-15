print("\n")

########################################################
def validateRecipeWithQuantity(fridge, ingredients):
    print(f"Ingredients = {ingredients}")
    print(f"Fridge = {fridge}")
    print("\n")
    print("#"*50)
    print("\n")
    counter = 0
    ingredients_length = len(ingredients)
    for k1,v1 in ingredients.items():
        for k2,v2 in fridge.items():
            if k1 == k2 and v1 == v2:
                counter += 1
            else:
                pass
    if counter == ingredients_length:
        return True
    else:
        return False
########################################################
""" This is gonna return False result """
ingredients = {'tomato': 1, 'onion': 2};
fridge = {'tomato': 1, 'onion': 1};

""" This is gonna return True result """
# ingredients = {'tomato': 2, 'onion': 3};
# fridge = {'tomato': 2, 'onion': 3, 'olives': 1};

results = validateRecipeWithQuantity(fridge, ingredients)
print(f"Result is = {results}")



print("\n\n")
