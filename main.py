import datetime
from pathlib import Path
import os.path
import json 
from commands import *

projects = {}

filename = "projects.json"
filepath = Path("projects.json")

if filepath.is_file():
	f = open("projects.json")
	data = json.load(f)
else:
	f = open("projects.json", 'w')
	f.write('{}')
	f.close()

projects = data

print("Welcome to the python project timer.\nType '--help' for a list of commands.\n")

command = input("What would you like to do?\n")
while (command != "quit" or "q"):
	if command == "list":
		list_projects(projects)
		command = get_command()
	elif command == "new":
		new_project(projects)
		command = get_command()
	elif command == "start timer":
		project_name = input("What is the name of your project?\n")
		if project_name in projects:
			start_timer(projects, project_name)
			command = get_command()
		else:
			print(f"A project by that name was not found.\n")
			command = get_command()
	elif command == "quit" or command == "q":
		quit()
	elif command == "clear":
		clear_all()
		command = get_command()
	elif command == "--help":
		print("The following are callable commands:\n")
		for n in commands:
			print(f"{n}")
		command = get_command()
	else:
		print("Sorry, the command wasn't found. For a list of commands \
			please type --help.")
		command = get_command()
