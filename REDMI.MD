# Personal Task Manager
![Static Badge](https://img.shields.io/badge/python-blue?logo=python&logoColor=white)
A simple task manager built with python

## Features
- add multiple books
- save books
- load saved books
- admin mode
  
## Requirments
- Python
- python-dotenv



## Project Structure
```task
personal_task_manager_main/
│   .env.example
│   .gitignore
│   main.py
│   README.md
│   requirements.txt
│   tasks.py
│
├───images
│       demo.gif
│       sc1.png
```

## Installaion
Install the requires packages:
```bash
python -m pip install -r requirements.txt
```


## Envoirment setup
create a `.env` as a template
Use `.env.example` as a template
Add your admin password
```env
BOOK_MANAGER_ADMIN_PASSWORD = your_password_here
```
replace `your_passsword_here` with your own admin password
## Run the programm
run the main file
```bash
python main.py
```
## Screenshot 
![personal_task_manager_screenshot](img\123.png)
