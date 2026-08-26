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
