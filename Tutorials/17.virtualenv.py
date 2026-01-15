## A virtual environemnet is like a seperate isolated python workspace for your project.
## It allows you to manage dependencies for different projects without conflicts.

'''
Imagine:
Project A requires package X version 1.0
Project B requires package X version 2.0
To avoid conflicts, we create separate virtual environments for each project.
If we install X globally, one project may break the other.


Without venv: All project share same installed libraried -> conflicts may arise
With venv: Each project has its own isolated environment -> no conflicts

steps to create and use a virtual environment:

1. Create a virtual environment:
   python -m venv myenv

2. Activate the virtual environment:
    on windows (power shell):
    myenv\Scripts\activate

    on Windows (CMD):
    myenv\Scripts\activate.bat

    If you get error “scripts disabled”, run:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    on macOS/Linux:
    source myenv/bin/activate

3. Install packages within the virtual environment:
   pip install package_name

4. Deactivate the virtual environment when done:
   deactivate

5. To delete the virtual environment, simply remove the myenv directory:
   rm -rf myenv  (macOS/Linux)

# Check installed packages in the virtual environment:
   pip list


'''