from king1234 import add_task,view_task,complete_task,delete_task,get_task_count,filter_by_subject,pending_task,completed_task,search_task,priority_medium,priority_low,task_deadline,study_statics,upcoming_tasks
import json
from datetime import datetime

today = datetime.today()

print(today)


import sqlite3

connection = sqlite3.connect("tasks.db")

print("Database connected!")

connection.close()

with (open("tasks.json","r") as file):
    tasks = json.load(file)


OPTION = """                     
                    ================================
                         STUDENT STUDY PLANNER
                    =================================

                             1. ADD TASK
                             2. VIEW TASKS
                             3. COMPLETE TASK
                             4. DELETE TASK
                             5. COUNT TASKS
                             6. SEARCH TASK
                             7. FILTER BY SUBJECT
                             8. PENDING TASKS
                             9. COMPLETED TASKS
                            10. PRIORITY MEDIUM
                            11. PRIORITY LOW
                            12. TASK DEADLINE
                            13. STUDY STATICS
                            14. UPCOMING TASKS
                            15. EXIT
                                                        """


while True:
    try:
        king = int(input(f"{OPTION}\n Enter your choice: "))

    except ValueError:
        print("Please enter a number 1 to 15")
        continue




    if king == 1:
        add_task(tasks)

    elif king == 2:
        view_task(tasks)

    elif king == 3:
        complete_task(tasks)

    elif king == 4:
        delete_task(tasks)

    elif king == 15:
        print("Thank you for using Student Study Planner")
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        break

    elif king == 5:
        count = get_task_count(tasks)
        print(count)

    elif king == 7:
        filter_by_subject(tasks)

    elif king == 8:
        pending_task(tasks)

    elif king == 9:
        completed_task(tasks)

    elif king == 6:
        search_task(tasks)

    elif king == 10:
        priority_medium(tasks)

    elif king == 11:
        priority_low(tasks)

    elif king == 12:
        task_deadline(tasks)

    elif king == 13:
        study_statics(tasks)

    elif king == 14:
        upcoming_tasks(tasks)

    else:
     print("Please enter a number 1 to 15")
