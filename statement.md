# Project Statement

## 1. Problem Statement

Students often have multiple academic tasks such as assignments, revision, projects, and study activities to complete within different deadlines. Managing these tasks manually can make it difficult to keep track of pending work, priorities, and upcoming deadlines.

The **Student Study Planner** is developed to provide a simple Python-based task management system that helps students organize and monitor their study activities. The system allows users to add, view, search, filter, complete, and delete study tasks while storing task information permanently using an SQLite database.

The project aims to make study planning easier by providing task priorities, deadlines, pending/completed task views, upcoming tasks, and study statistics.

## 2. Scope of the Project

The scope of the Student Study Planner includes managing academic study tasks through a command-line Python application.

The system covers:

* Creating and storing study tasks.
* Assigning a subject to each task.
* Setting deadlines using the `DD-MM-YYYY` format.
* Assigning task priorities such as High, Medium, and Low.
* Viewing all stored tasks.
* Marking tasks as completed.
* Deleting tasks.
* Searching for tasks using keywords.
* Filtering tasks by subject.
* Viewing pending and completed tasks separately.
* Viewing tasks according to priority.
* Checking tasks for specific deadlines.
* Displaying upcoming pending tasks.
* Generating study statistics such as total, completed, pending, priority distribution, progress percentage, overdue tasks, and tasks due today or tomorrow.
* Storing task data permanently using SQLite.

The current project is designed as a local command-line application and does not include online synchronization, multi-user accounts, or a web/mobile interface.

## 3. Target Users

The primary target users are:

### Students

Students can use the application to organize assignments, study activities, projects, revision tasks, and other academic work.

### School and College Students

The planner can help students manage multiple subjects and keep track of deadlines and priorities.

### Beginners Learning Python

The project can also be useful for beginners who want to understand practical Python concepts such as functions, modules, exception handling, file handling, SQLite databases, SQL queries, and application structure.

### Individual Users

Any individual who wants a simple local task-management system for organizing study-related activities can use the application.

## 4. High-Level Features

### 4.1 Add Study Tasks

Users can create a task by entering:

* Subject
* Task description
* Deadline
* Priority

The application validates the entered date and priority before storing the task.

### 4.2 View All Tasks

Users can view all saved study tasks along with their:

* Task ID
* Subject
* Task description
* Date
* Priority
* Status

### 4.3 Complete Tasks

Users can select a task using its ID and mark it as completed.

### 4.4 Delete Tasks

Users can remove an existing task from the database using its task ID.

### 4.5 Search Tasks

Users can search for tasks using keywords. The search can match information such as subject, task description, date, priority, or status.

### 4.6 Filter by Subject

Users can enter a subject name and view tasks associated with that subject.

### 4.7 Pending and Completed Tasks

The application provides separate views for:

* Pending tasks
* Completed tasks

This makes it easier to understand the user's remaining workload.

### 4.8 Priority Management

Tasks can be categorized as:

* High Priority
* Medium Priority
* Low Priority

Users can view tasks according to their priority.

### 4.9 Deadline Management

Users can search for tasks associated with a specific deadline and identify tasks that are due soon.

### 4.10 Upcoming Tasks

The system can display pending tasks whose dates are today or in the future, helping users identify upcoming academic work.

### 4.11 Study Statistics

The application provides study statistics including:

* Total number of tasks
* Completed tasks
* Pending tasks
* Completion progress percentage
* High-priority tasks
* Medium-priority tasks
* Low-priority tasks
* Overdue tasks
* Tasks due today
* Tasks due tomorrow

### 4.12 SQLite Database

The project uses SQLite to permanently store task information. The database stores fields including task ID, subject, task description, date, priority, and status.

## 5. Technologies Used

* **Python** — Application development
* **SQLite** — Persistent task storage
* **SQL** — Database operations
* **JSON** — Task data handling in the application
* **Git & GitHub** — Version control and project management
