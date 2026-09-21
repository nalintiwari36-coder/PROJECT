from database import (
    add_task_db,
    get_tasks,
    complete_task_db,
    delete_task_db,
    count_tasks_db,
    search_task_db,
    filter_subject_db,
    pending_tasks_db,
    completed_tasks_db,
    medium_priority_db,
    low_priority_db,
    deadline_tasks_db,
    upcoming_tasks_db
)

from datetime import datetime, timedelta




def print_tasks(tasks):

    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:

        print(
            "ID:", task[0],
            "| Subject:", task[1],
            "| Task:", task[2],
            "| Date:", task[3],
            "| Priority:", task[4],
            "| Status:", task[5]
        )




def add_task():

    try:

        subject = input("SUBJECT: ").strip()

        if not subject:
            print("Subject cannot be empty.")
            return

        task = input("TASK: ").strip()

        if not task:
            print("Task cannot be empty.")
            return

        date = input("DATE (DD-MM-YYYY): ").strip()

        try:
            datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            print("Invalid date.")
            print("Please enter date in DD-MM-YYYY format.")
            return

        priority = input(
            "PRIORITY (High/Medium/Low): "
        ).strip().capitalize()

        if priority not in ["High", "Medium", "Low"]:

            print("Invalid priority.")
            print("Please enter High, Medium or Low.")
            return

        add_task_db(
            subject,
            task,
            date,
            priority
        )

        print("Task added successfully.")

    except Exception as error:

        print("Something went wrong:", error)



def view_task():

    try:

        tasks = get_tasks()

        print("\n========== ALL TASKS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)




def complete_task():

    try:

        tasks = get_tasks()

        print("\n========== ALL TASKS ==========")

        print_tasks(tasks)

        if not tasks:
            return

        task_id = int(
            input("Enter task ID to complete: ")
        )

        complete_task_db(task_id)

    except ValueError:

        print("Please enter a valid number.")

    except Exception as error:

        print("Something went wrong:", error)



def delete_task():

    try:

        tasks = get_tasks()

        print("\n========== ALL TASKS ==========")

        print_tasks(tasks)

        if not tasks:
            return

        task_id = int(
            input("Enter task ID to delete: ")
        )

        delete_task_db(task_id)

    except ValueError:

        print("Please enter a valid number.")

    except Exception as error:

        print("Something went wrong:", error)



def get_task_count():

    try:

        count = count_tasks_db()

        print("Total tasks:", count)

    except Exception as error:

        print("Something went wrong:", error)



def search_task():

    try:

        search = input(
            "Please enter your search: "
        ).strip()

        if not search:

            print("Search cannot be empty.")
            return

        tasks = search_task_db(search)

        print("\n========== SEARCH RESULTS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)



def filter_by_subject():

    try:

        subject = input(
            "Please enter your subject: "
        ).strip()

        if not subject:

            print("Subject cannot be empty.")
            return

        tasks = filter_subject_db(subject)

        print("\n========== SUBJECT TASKS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)



def pending_task():

    try:

        tasks = pending_tasks_db()

        print("\n========== PENDING TASKS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)




def completed_task():

    try:

        tasks = completed_tasks_db()

        print("\n========== COMPLETED TASKS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)




def priority_medium():

    try:

        tasks = medium_priority_db()

        print("\n========== MEDIUM PRIORITY ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)




def priority_low():

    try:

        tasks = low_priority_db()

        print("\n========== LOW PRIORITY ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)



def task_deadline():

    try:

        date = input(
            "Enter deadline (DD-MM-YYYY): "
        ).strip()

        try:

            datetime.strptime(
                date,
                "%d-%m-%Y"
            )

        except ValueError:

            print("Invalid date.")
            print("Please use DD-MM-YYYY format.")
            return

        tasks = deadline_tasks_db(date)

        print("\n========== DEADLINE TASKS ==========")

        print_tasks(tasks)

    except Exception as error:

        print("Something went wrong:", error)




def study_statics():

    try:

        tasks = get_tasks()

        if not tasks:

            print("No tasks available.")
            return

        today = datetime.today().date()

        tomorrow = today + timedelta(days=1)

        total = len(tasks)

        completed = 0
        pending = 0

        high = 0
        medium = 0
        low = 0

        overdue = 0
        due_today = 0
        due_tomorrow = 0

        for task in tasks:

            status = task[5]
            priority = task[4]
            date = task[3]

            # Status

            if status == "completed":

                completed += 1

            elif status == "pending":

                pending += 1

            # Priority

            if priority == "High":

                high += 1

            elif priority == "Medium":

                medium += 1

            elif priority == "Low":

                low += 1

            # Date

            try:

                task_date = datetime.strptime(
                    date,
                    "%d-%m-%Y"
                ).date()

                if task_date < today and status == "pending":

                    overdue += 1

                elif task_date == today:

                    due_today += 1

                elif task_date == tomorrow:

                    due_tomorrow += 1

            except ValueError:

                continue

        progress = (completed / total) * 100

        print("""
========================================
           STUDY STATISTICS
========================================
""")

        print("Total Tasks       :", total)
        print("Completed         :", completed)
        print("Pending           :", pending)
        print(f"Progress          : {progress:.2f}%")

        print()

        print("High Priority     :", high)
        print("Medium Priority   :", medium)
        print("Low Priority      :", low)

        print()

        print("Overdue           :", overdue)
        print("Due Today         :", due_today)
        print("Due Tomorrow      :", due_tomorrow)

        print("""
========================================
""")

    except Exception as error:

        print("Something went wrong:", error)



def upcoming_tasks():

    try:

        tasks = upcoming_tasks_db()

        print("\n========== UPCOMING TASKS ==========")

        if not tasks:

            print("No upcoming tasks.")
            return

        today = datetime.today().date()

        found = False

        for task in tasks:

            try:

                task_date = datetime.strptime(
                    task[3],
                    "%d-%m-%Y"
                ).date()

                if task_date >= today and task[5] == "pending":

                    print(
                        "ID:", task[0],
                        "| Subject:", task[1],
                        "| Task:", task[2],
                        "| Date:", task[3],
                        "| Priority:", task[4]
                    )

                    found = True

            except ValueError:

                continue

        if not found:

            print("No upcoming tasks.")

    except Exception as error:

        print("Something went wrong:", error)