from supabase import create_client, client
import os
from dotenv import load_dotenv
from tabulate import tabulate as tb
import authentication as auth


load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)


def add_todo():
    # global current_user
    if current_user == None:
        print("Pls signed in first")
        return
    user_id = current_user["id"]
    task = input("Enter your task: ")
    is_completed = False
    response = (
    supabase.table("Todo")
    .insert({"to_do": task, "completed": is_completed,"user_id":user_id})
    .execute()
)
    # if response:
    #     print("ToDo has been added successfully")
    # elif response.error:
    #     print("Error: ", response.error)
    if response.data:
        print("Data has been added successfully")
            


def delete_task():
    show_data()
    index = int(input("Enter the id to delete the task: "))
    response = (
    supabase.table("Todo")
    .delete()
    .eq("id", index)
    .execute()
)
    print(response)
    print(f"{index} task has been deleted !")


def update_task():
    data = show_data()
    index = int(input("Enter the index number to complete: "))
    for item in data:
        if item["id"]==index:
            if not item["completed"]:
               response = (
    supabase.table("Todo")
    .update({"completed":True})
    .eq("id", index)
    .execute()
)   
    print("Task has beedn updated successfully !")


def show_data():
    is_complete = {False: "not completed", True:"done"}
    response = (
    supabase.table("Todo")
    .select("*")
    .execute()
)
    data = response.data or []
    table = []
    for item in data:
        status = is_complete.get(item["completed"], "unknown")
        print(f'{item["id"]}: {item["to_do"]} → {status}')
        table.append([item["id"], item["to_do"], status])
    headers = ["ID", "Task", "Status"]
    print(tb(table, headers=headers, tablefmt="grid"))
    return data

is_log_in = False
running = True

if __name__ == '__main__':
    current_user = None
    while not is_log_in:
        print("1 to sign in: ")
        print("2 to sign up: ")
        authentication_option = int(input("Select option: "))

        if authentication_option == 1:
            current_user = auth.sign_in()
            if current_user:
                is_log_in == True
        
        elif authentication_option == 2:
            current_user = auth.sign_up()
            if current_user:
                is_log_in == True
        else:
            print("Invalid option. Pls try again")
        break
    
    while running:
        print("Enter 1 to add to do")
        print("Enter 2 to complete the task")
        print("Enter 3 to delete the task")
        print("Enter 4 to update the task")
        print("Enter 5 to show the tasks")
        print("Enter 6 to exit")

        choice = int(input("Enter your choice: "))
        if choice == 1: add_todo()
        elif choice == 2: pass
        elif choice == 3: delete_task()
        elif choice == 4: update_task()
        elif choice == 5: show_data()
        elif choice == 6:
            print("Exiting...")
            running = False
        else: print("Pls enter a valid input: ")
    
    
