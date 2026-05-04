"""

Challenge: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
   - Add a task
   - View all tasks
   - Mark a task as completed
   - Delete a task
   - Exit the app
2. Save all tasks in a text file named `tasks.txt` so data persists between runs.
3. Display tasks with an index number and a ✔ if completed.

Example menu:
1. Add Task  
2. View Tasks  
3. Mark Task as Completed  
4. Delete Task  
5. Exit

Example output:
Your Tasks:

Buy groceries||not_done
Finish Python project||done
Read a || book||not_done


Bonus:
- Prevent empty tasks from being added
- Validate task numbers before completing/deleting

"""

import os

task_file = " tasks.txt "

def add_task():
    tasks = []
    if (os.path.exists(task_file )):
        with open(task_file , "r" , encoding= "utf-8" ) as f :
            for line in f:
               text , status = line.strip().rsplit("||" , 1)
               tasks.append({"text" : text , "done" : status =="done"})
    return tasks

def save_task(tasks):
    with open(task_file , "w" , encoding= "utf-8") as f:
      for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']}||{status}\n")

def display_task(tasks):
    if not tasks:
        print("\n No task not found")
    else:
     for i , task in enumerate(tasks , 1):  #automatic numeric update like count+=1
        checkbox = "✅" if task['done'] else " "
        print(f"{i}.{checkbox} {task['text']}")
print()               #new line

def tasklist_manager():
   tasks = add_task()

   while True:
      print("\n________________TaskList_Manager________________")
      print("1.Add task")
      print("2.View task")
      print("3.Mark as task completed")
      print("4.Delete task")
      print("5.Exit TaskList Manager")

      choice = input("Choose an option (1-5)").strip()

      match choice:
         case "1":
            text = input("Enter your task").strip()
            if text:
               tasks.append({"text":text , "done":False})
               save_task(tasks)
            else:
               print("Task cannot be empty")
         case "2":
            display_task(tasks)
         case "3":
            display_task(tasks)
            try:
               num= int(input("Enter your task number to mark as completed! \n"))
               if 1 <= num <= len(tasks) :
                  tasks[num-1]["done"] = True
                  save_task(tasks)
                  print("Task is completed")
               else:
                  print("Task is incompleted")
            except ValueError:
               print("Please enter a number")
         case "4":
             display_task(tasks)
             try:
                 num= int(input("Enter your task number to delete! \n"))
                 if 1 <= num <= len(tasks):
                     removed = tasks.pop(num-1)
                     save_task(tasks)
                     print(f"The task delete {removed['text']}")
                 else:
                     print("Invalid task number")
             except ValueError:
                  print("Please enter a number")
         case "5":
            print("Exit from the TaskList Manager\n")
            break
         case _ :
            print("Invalid choice")
         
tasklist_manager()


    
   
    