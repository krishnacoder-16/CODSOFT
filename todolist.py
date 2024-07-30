l=[]
while True:
      print("select operation\n1.Insert the task\n2.Show the task\n3.Delete the task\n4.Mark task as done\n5.Exit")
      c=int(input("Enter the no. of operation:"))
      if c==1:
             n_tasks=int(input("How many task you want to add:"))
             for i in range(n_tasks):
                   task = input("Enter the task: ")
                   l.append({"task": task, "done": False})
                   print("Task added!")
      elif c == 2:
        print("\nTask:")
        for index, task in enumerate(l):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")
      elif c==3:
           if task in l:
                 l.remove(task)
                 print(f"Task removed: {task}")
           else:
               print(f"Task not found: {task}")
      elif c == 4:
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(l):
            l[task_index]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
      elif c == 5:
            print("Exiting the To-Do List.")
            break

      else:
          print("Invalid choice. Please try again.")