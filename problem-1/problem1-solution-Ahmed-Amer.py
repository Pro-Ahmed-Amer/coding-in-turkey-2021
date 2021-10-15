print("\n")

############################################
def validateRecipe(fridge, ingredients):
    ingredients_counter = len(ingredients)
    counter = 0
    for i in ingredients:
        for j in fridge:
            if i in j:
                counter += 1
            else:
                pass
    if counter == ingredients_counter:
        return True
    else:
        return False
############################################


""" First Check = False """
ingredients = ['tomato', 'onion', 'lettuce']
fridge = ['tomato', 'banana', 'apple', 'onion', 'cucumber']


""" Second Check = True """
# ingredients = ['olives', 'onion', 'lettuce']
# fridge = ['onion', 'banana', 'lettuce', 'olives']


result = validateRecipe(fridge, ingredients)
print(f"Result is = {result}")


print("\n\n")
