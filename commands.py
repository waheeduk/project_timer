def get_command():
	command = input("What would you like to do?")
	return command

def list_projects(project_list):
	print("The list of projects are as follows\n")
	if len(project_list) == 0:
		print("You don't have any projects right now.")
	else:
		print(projects)

def new_project(project_list):
	name = input("What is the name of your project?")
	project_list[str(name)] = 0

def start_timer(project_name):
	time_now = datetime.datetime.now()
	detect_stop = input("Enter 'stop' to stop recording.\n")
	if detect_stop == "stop":
		time_finished = datetime.datetime.now()
		total_time = time_finished - time_now
		seconds = total_time.total_seconds()
		projects[project_name] += seconds
		json_object = json.dumps(projects, indent = 4)
		with open(filename, 'w') as outfile:
			outfile.write(json_object)

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
"quit -- exit the programme"]