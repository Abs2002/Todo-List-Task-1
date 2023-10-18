#usr/bin/python3

'''
task 1 : to create a todo list in cli
given actions to perform are create, view, mark tasks complete, delete a task
simple and innovative cli application
'''

#importing the appropiate libraries
import mysql.connector #to make connection with mysql database
import random # to generate random numbers
from datetime import date #to get date
import time #to use time

#to make table in cli
from rich.console import Console
from rich.table import Table


class todolist:
    #contructor initialized for future purposes
    def __init__(self):
        pass

    #method to add a task
    def add_task(self):
        try:
            print("You have selected to add a task in your list")
            task_name=input("Enter the task name : ")
            task_description=input("Enter the task Description : ")
            current_time=time.strftime("%H:%M:%S")
            database_cursor.execute(f"insert into todolist1 values('{random.randint(100,1000)}','{task_name}','{task_description}','Not Completed','{date.today()}','{current_time}')")
            database_name.commit()
            print("Task Added")
        except:
            print("error encountered")

    #method to view all tasks
    def view_tasks(self):
        try:
            database_cursor.execute("select *from todolist1")
            task_list=database_cursor.fetchall()

                #print("Task_ID\tTask_Date\tTask_time\tTask_name\tTask_description\tTask_status")
                #for i in task_list:
                    #print(i[0],"\t",i[4],"\t",i[5],"\t",i[1],"\t",i[2],"\t",i[3])
            table = Table(title="Task Table")
            task_list=list(task_list)
            columns = ["Task_ID", "Task_name", "Task_description", "Task_status", "Task_date", "Task_time"]


            for column in columns:
                table.add_column(column)

            for row in task_list:
                table.add_row(*row, style='bright_green')
            console = Console()
            console.print(table)
            print("===============================================================================")
        except:
            print("error encountered")
    #method to mark the task complete
    def marktask_complete(self):
        #to fetch all the tasks from the db
        try:
            database_cursor.execute("select task_id, task_name from todolist1")
            task_list=database_cursor.fetchall()
            #print("Task_No.\tTask_name")
            #print(task_list)
            #for i in range(len(task_list)):
            #    print(task_list[i][0], "\t", task_list[i][1])
            table = Table(title="Task Table")
            task_list = list(task_list)
            columns = ["Task_ID", "Task_name"]

            for column in columns:
                table.add_column(column)

            for row in task_list:
                table.add_row(*row, style='bright_green')
            console = Console()
            console.print(table)

            task_number=int(input("Enter the Task Number you want to mark complete : "))
            #task_name2=task_list[task_number-1]
            database_cursor.execute(f"update todolist1 set task_status='Completed' where task_id='{task_number}'")
            database_name.commit()
            print("Task Successfully marked as Completed")
            print("===============================================================================")
        except:
            print("===============================================================================")
            print("Error found here")
            print("please try again some time")
            print("===============================================================================")


    #method to delete the task
    def delete_task(self):
        try:
            #to fetch all the tasks from the db
            database_cursor.execute("select task_id, task_name from todolist1")
            task_list = database_cursor.fetchall()
            print("Task_No.\tTask_name")
            # print(task_list)
            #for i in range(len(task_list)):
            #    print(task_list[i][0], "\t", task_list[i][1])
            table = Table(title="Task Table")
            task_list = list(task_list)
            columns = ["Task_ID", "Task_name"]

            for column in columns:
                table.add_column(column)

            for row in task_list:
                table.add_row(*row, style='bright_green')
            console = Console()
            console.print(table)
            task_number=int(input("Enter the Task Number you want to delete : "))
            database_cursor.execute(f"delete from todolist1 where task_id='{task_number}'")
            database_name.commit()
            print("Task successcully deleted")
            print("===============================================================================")
        except:
            print("===============================================================================")
            print("Error found here")
            print("Please Try again")
            print("===============================================================================")



if __name__ == '__main__':
    # creating a valid Mysql Connection (global vars declared)
    database_name = mysql.connector.connect(user="root", password="root123", host="127.0.0.1", database="todolist")
    database_cursor = database_name.cursor()
        #creating a menu bar where user has to choose the option
    userchoice_number=0
    todolist_object=todolist()
    print("===============================================================================")
    print("Welcome to the Todo List Application CLI version")
    print("===============================================================================")
    while(1==1):
        try:
            print(" ")
            print("Enter the desired option from the drop down menu down below : ")
            print(" ")
            print("Press 1 to Add tasks")
            print("Press 2 to View tasks")
            print("Press 3 to Mark a task as completed")
            print("Press 4 to Delete a task ")
            print("Press 5 to exit the application")
            print("===============================================================================")
            print(" ")
            userchoice_number=int(input("Enter a valid response : "))
            print(" ")
            if(userchoice_number==1):
                todolist_object.add_task()
            elif(userchoice_number==2):
                todolist_object.view_tasks()
            elif(userchoice_number==3):
                todolist_object.marktask_complete()
            elif(userchoice_number==4):
                todolist_object.delete_task()
            elif(userchoice_number==5):
                print("Thank you for using the Task Manager")
                break
            else:
                print("The response is invalid and cannot be accepted Try again")
                print(" ")
        except:
            print("error occoured here")
    print("Thank you for Using Task Management Application")
    database_name.close()