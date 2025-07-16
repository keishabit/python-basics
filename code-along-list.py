# create an empty list

todo_list = []
print("Your todo list", todo_list)

# append items to the list

todo_list.append("Buy groceries")
todo_list.append("Study")
todo_list.append('Get gifts')

print("Updated list:", todo_list)

# insert an item 

todo_list.insert(1, "Pay the bills")
print("After inserting an imem:", todo_list)

# Using indexes and slicing

print("First task:", todo_list[0])
print("Last two tasks:", todo_list[-2:])

# mark a task as done

done_task = todo_list.pop(2)
print("You completed:", done_task)
print("Todo list after removal:",todo_list)

# update a existing task

print(todo_list[1])
todo_list[1] = "Buy groceries and snacks"
print("Updated todo list value:", todo_list)

# print a task list

print("Here's what you still need to do:")
for task in todo_list:
    print("-", task)