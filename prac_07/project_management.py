"""
Estimate: 1hr
Actual:
"""

from datetime import datetime
from project import Project

FILENAME = "projects.txt"


def main():
    projects = load_data(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} from {FILENAME}")
    menu_choice = input(
        "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects\n(A)dd project\n(U)pdate project\n(Q)uit\n>>> ").lower()
    while menu_choice != "q":
        if menu_choice == "l":
            file_name = input("File name: ")
            projects = load_data(file_name)
        elif menu_choice == "s":
            file_name = input("File name: ")
            save_data(projects, file_name)
        elif menu_choice == "d":
            display_projects(projects)
        elif menu_choice == "f":
            filter_projects(projects)
        elif menu_choice == "a":
            add_project(projects)
        elif menu_choice == "u":
            update_project(projects)
        else:
            print("Invalid menu choice.")
        menu_choice = input(
            "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects\n(A)dd project\n(U)pdate project\n(Q)uit\n>>> ").lower()
    save_choice = input(f"Would you like to save to {FILENAME}?").lower()
    if save_choice.startswith("y"):
        save_data(projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def load_data(file_name):
    projects = []
    in_file = open(file_name, "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split("\t")
        name, start_date, priority, cost_estimate, completion_percentage = parts
        project = Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage))
        projects.append(project)
    in_file.close()
    return projects


def save_data(projects, file_name):
    out_file = open("projects.txt", "r")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}")
    out_file.close()


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    complete_projects = [project for project in projects if project.completion_percentage == 100]
    incomplete_projects.sort()
    complete_projects.sort()
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"    {project}")
    print("Completed projects:")
    for project in complete_projects:
        print(f"    {project}")


def filter_projects(projects):
    date_str = input("Show projects that start after the date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    for project in projects:
        start_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if start_date >= filter_date:
            print(project)


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_percent = input("New Percentage: ")
    if new_percent != "":
        project.completion_percentage = int(new_percent)
    new_priority = input("New Priority: ")
    if new_priority != "":
        project.priority = int(new_priority)


main()
