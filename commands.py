import datetime
from pathlib import Path
import json
filename = "projects.json"

def get_command():
	command = input("What would you like to do?")
	return command

def list_projects(project_list):
	print("The list of projects are as follows\n")
	if len(project_list) == 0:
		print("You don't have any projects right now.")
	else:
		for x, y in project_list.items():
			print(f"Project Title: {x}")
			hour = 0
			min = 0
			sec = 0
			hour = y // (60 * 60)
			min = (y - (hour * 3600)) // 60
			sec = y - (hour*3600) -( min*60)
			sec = sec // 1
			print(f"Time spent is: {int(hour)} hours {int(min)} minutes and {int(sec)} seconds.")

def new_project(project_list):
	name = input("What is the name of your project?")
	while name not in project_list:
		project_list[str(name)] = 0
	else:
		name = input("A project by that name already exists. Please pick \
			another name.\n")

def start_timer(project_list, project_name):
	time_now = datetime.datetime.now()
	detect_stop = input("Enter 'stop' to stop recording.\n")
	if detect_stop == "stop":
		time_finished = datetime.datetime.now()
		total_time = time_finished - time_now
		seconds = total_time.total_seconds()
		project_list[project_name] += seconds
		json_object = json.dumps(project_list, indent = 4)
		with open(filename, 'w') as outfile:
			outfile.write(json_object)

def delete(project_list, project_name):
	if project_name in project_list:
		del project_list[project_name]
	else:
		print(f"No project called {project_name} was found.")

def clear_all():
	filepath = Path("projects.json") 
	if filepath.is_file():
		f = open("projects.json", 'w')
		f.write('{}')
		f.close()

def quit():
	raise SystemExit

commands = ["list -- list all current projects", "new -- create a new project", \
"start timer -- start a timer for a currently listed project", "clear -- delete all projects",\
"delete -- delete a project", "quit -- exit the programme"]