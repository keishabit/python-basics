# play with for loops

# create a list

# use for loop to iterate through the list

goals_chart = []
print("Your Weekly Goals", goals_chart)

# append items to the list

goals_chart.append("Start something new")
goals_chart.append("Grow a plant")
goals_chart.append('Get gifts')

print("Your Weekly Goals:", goals_chart)

# insert an item 

goals_chart.insert(1, "Go for walk")
print("After inserting an imem:", goals_chart)

# Using indexes and slicing

print("First task:", goals_chart[0])
print("Last two tasks:", goals_chart[-2:])

# mark a task as done

done_task = goals_chart.pop(2)
print("You completed:", done_task)
print("Goals after removal:",goals_chart)

# update a existing task

print(goals_chart[1])
goals_chart[1] = "Be kind to self & others"
print("Updated goals chart value:", goals_chart)

# print a task list

print("Here's what you still need to do:")
for task in goals_chart:
    print("-", task)