# what is virtual environment??
when you have different version of library install and the one who is working with you have different version , there might occur many errors
---
# your pc can work either global or virtual
why to work on 2 different env 
cuz virtual is isolated and doesn't involve with outside world
for example
i have installed both the pandas version and i am using it but python script doesnt know which version to implement so to overcome this shitt 
we create a virtual env which is isolated from global one and we just download everything inside that like a new env which knows ntg
# how to create that thing
- create new folder for env
```bash
python -m venv FILE_NAME
```
- activate the venv(virtual env ) you created
# for windows in terminal
```bash
FILE_NAME\Scripts\activate.bas
```
# in powershell
```bash
FILE_NAME\Scripts\activate.ps1
```
# in MAC/LINUX
```bash
source FILE_NAME\bin\activate
```
# to deactivate your env
- if you are inside that activated env
```bash
deactivate
```
- if you want to deactivate some other activated env
```bash
.\venv\Scripts\deactivate.bat
```
---
# what is requirement.txt??
so basically when you create a virtual env for your python script and someone is asking for your project to execute in there pc and are asking which version to install in their pc 
now you dont have to check each and every info just to acknowledge him/her

- this command will show you what all are installed in your global or venv with versions
```bash
pip freeze
```
- now to put all this in one file we just create a txt file which contains all the requirements
```bash
pip freeze > requirements.txt
```
- now to install all those requirements in your pc we just use
```bash
pip install -r requirements.txt
```

