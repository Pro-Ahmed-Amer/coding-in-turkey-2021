print("\n")

############################################### First Way

def whereIsMyFood(fridge, item):
    flag = -1
    for i in range(len(fridge)):
        if fridge[i] == item:
            flag = 1
            return (i)
    if flag == -1:
        return -1

############################################### Second Way "Plz, Remove the comment and stop the first way"
"""
def whereIsMyFood(fridge, item):
    if item in fridge:
        return (fridge.index(item))
    else:
        return (-1)
"""
############################################### Start Point

fridge_items = ["item1", "item2", "item3", "item4", "item5", "item6"]


# direct way search about this element
check_item = "item3"


# Ask the user about what he wanna search
# check_item = input("Enter What You Searching about : ")


# Print the final result
result = whereIsMyFood(fridge_items,check_item)
print(f"You Search about [{check_item}]\nResult = {result}")




print("\n\n")
