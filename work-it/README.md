# Work-It :alarm_clock:

Hey folks, I am Work-It, your personal task manager discord bot. :robot: 

## :scroll: Menu 

- [Usage](#Usage)
- [Setup](#Setup)

## Usage

### Adding a task: 
To add a task, use the command  
```
!task add <task-name> <start-time> <start-date> <end-time> <end-date>

Example: !task add task-name 10:30 10-09-2020 10:30 15-09-2020
```


### View tasks:
To view task, use this command  
```
!task view
```

### Complete task:
To delete a task, use this command  
```
!task complete <id>

Example: !task complete 1599672029
```

### Snooze task:
To advance the end-time, use this command  
```
!task snooze <id> <new-date>

Example: !task snooze 1599672029 20-09-2020
```


## Setup 

1. Clone the repository using
```git clone <link>``` or download and extract the zip file.

2. To get the python packages installed, simply run  
```pip install -r requirements.txt```

3. Create a .env file in project directory and place varName = value in there  
***Example***:  
DISCORD_TOKEN = 'XXXXXX'  
To get the token, go to Discord developer portal. If you already have a bot created, click it in the list, else create a New Application, give it a name and retrieve token.  
