import db_helper



def main():
    db_helper.create_table()
    run=1

    while run:
        print("Press 1: To add task")
        print("Press 2: To fetch task")
        print("Press 3: To delete task")
        print("Press 4: To update task")
        print("Press 5: To exit")

        ch=input("Enter your choice: ")

        if ch=="1":
            todo=input("enter your task: ")
            db_helper.add_task(todo)
        elif ch =='2':
            db_helper.display_task()
        
        elif ch=='3':
            ind=int(input("enter id of todo to be deleted: "))
            db_helper.delete_task(ind)
        elif ch=='4':
            ind=int(input("enter id of todo to be deleted: "))
            updated_task=input("Enter updated task: ")
            db_helper.update_task(ind,updated_task)
        elif ch=='5':
            run=0

    db_helper.close_connection()


if __name__ == "__main__":
    main()