"# SDEV265_Project" 

1.	Install Python - Python is the backbone of Django, so installing it is one of the first things you should do. You can find the latest version of Python here: https://www.python.org/downloads/ (be sure to check “add Python to PATH”)
2.	Download Red Team’s Blog code - To do this you can head to our team leader’s Github: https://github.com/AeCohill/sdev265_Blog Hit the “Code” button and click “Download ZIP.” 
3.	Extract ZIP and add to your computer drive - Unzip the files and place them into your Windows C: (or whatever your local operating system c-drive is)
4.	Open your local command prompt (for Windows you can type CMD into the Windows search bar) and change the directory to our project folder by entering the following commands: “ cd \” then follow with a “cd {name of your folder}” *Note: The brackets aren’t needed. 
5.	Now you’ll have to run the virtual environment. First to create a Virtual environment, enter the following command: -m venv myvenv 
6.	Next to activate it, enter this command: “myvenv\Scripts\activate”  (there should now be a (myvenv) before C: in your command prompt)	 
7.	Now you’ll have to install Django. First, enter “pip install --upgrade pip ” into the command line, and follow on-screen instructions.
8.	After that loads up and requirements are satisfied, on the next command line, enter “pip install django” The command prompt should say something along the lines of “Successfully installed Django”
9.	Now download the latest version of Pillow (pillow · PyPI) by entering “pip install pillow” into the command prompt. (it may have you enter another command, so follow the on-screen instructions) 
10.	Now we are ready to run this thing! Enter “python manage.py runserver” into the command prompt, and when successfully running hold Ctrl and click the server link given by the CMD to open our site in your default browser.
11.	Voila! Enjoy the blog.
