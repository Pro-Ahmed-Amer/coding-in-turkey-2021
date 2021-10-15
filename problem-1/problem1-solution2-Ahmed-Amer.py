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

ingredients = []
fridge = ['tomato', 'banana', 'apple', 'onion', 'cucumber']
i = 0
x = ""

print("=========== Type \'end\' To Finish !!! ===========\n")
############################################ To Read ingredients from chef
while x != "end":
    x = input("Enter ingredients : ")
    if x != "end":
        ingredients.append(x)
    else:
        pass
    i += 1

############################################ To Print The Result
result = validateRecipe(fridge, ingredients)
print(f"Result is = {result}")


print("\n\n")
