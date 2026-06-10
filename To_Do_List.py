tasks = []
while True:
 print("1.Add 2.Show 3.Exit")
 choice = input("Choose: ")
 if choice == "1":
  task = input("Task: ")
  tasks.append(task)
  print("Added!")
 elif choice == "2":
  print(tasks)
 else:
  break
