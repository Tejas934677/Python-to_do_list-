def main():
    tasks =[]
    
    while True:
        print("**********to-do list**********")
        print("1.add ask")
        print("2.show task")
        print("3.mark task as Done ")
        print("4.exit")
        
        
        choice = input("enter your choice:")
        
        if choice == '1':
            print()
            n_tasks = int(input("how many task you want to add:"))
            
            for i in range(n_tasks):
                task = input("enter the task")
                tasks.append({"task":task,"done":False})
                print("task added! ")
                
        
        elif choice == '2':
        
            print("\nTask:")
            for index,task in enumerate(tasks):
                status = "done" if task["done"] else "Not done "
                print(f"{index+1}.{task['task']}-{status}")

        elif choice =='3':
            task_index = int(input("enter the task number to mark as done :"))-1
            if 0<= task_index < len(tasks):
                tasks[task_index]["done"] = True 
                print("Task marked as done!")
            else:
                print("invalid task number.")
                
                
        elif choice == '4':
            print("exitig the to-do-list.")
            break
        
        else:
            print("invalid choice.please try again ")
main()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
