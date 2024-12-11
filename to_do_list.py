to_do_list = ["Buy groceries", "Clean house", "Pay bills"]

# adding to task
to_do_list.append("Schedule meeting")
to_do_list.append("Go for walk")


# removing a completed task

to_do_list.remove("Clean house")

# Checking if a task is in the list

if "Pay bills" in to_do_list:
    print("Don't forget to pay the internet bill.")


print("To do list remaining:")
for task in to_do_list:
    print(f"-{task}")
