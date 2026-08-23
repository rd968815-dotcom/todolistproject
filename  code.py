list_of_tasks=["python basics","python intermediate","python advance","python developer"]
while(True):
  print("to do list menu")
  print("1.add task")
  print("2.view tasks")
  print("3.completed tasks")
  print("4.delete task")
  print("5.exit")
  user_choice = int(input("enter your choice"))
  if user_choice==1:
      print("add task")
      list_of_tasks.append(input("enter the task"))
  elif user_choice==2:
      print("view task")
      print(list_of_tasks)
  elif user_choice==3:
      print("completed tasks")
      completed_tasks=input("enter your completed tasks")
      if completed_tasks in list_of_tasks:
        print("this task is completed")
  elif user_choice==4:
    print("delete task")
    deleted_task=input("enter your deleted task")
    if deleted_task in list_of_tasks:
        list_of_tasks.remove(deleted_task)
        print("your task is deleted")
  elif user_choice==5:
    print("exit")
    break
  else:
    print("no task in this list")