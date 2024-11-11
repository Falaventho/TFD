# Developer Guide

General guidelines for setting up your workspace to contribute to the project.

## Git

To contribute to this project, you need to use git. If you have git installed, great! Otherwise, you can [download it here](https://git-scm.com/downloads). Once you have git, you need to clone the repository. To clone the repository, navigate to the place you want to work using a terminal (the built-in terminal for VSCode works great) and run the following command:

```bash
git clone https://github.com/Falaventho/TFD
```

Once you have it cloned, navigate to the directory with this command:

```bash
cd TFD
```

And switch to your branch like this:

```bash
git checkout myBranch
```

Now you're (almost) ready to go!

## Python Packages

To keep things neat and tidy, Python has 'virtual environments' that allow for workspace-based module installation. Whenever a module is added, everyone working on the project needs to install it. The list of current modules is found in 'requirements.txt' which pip (python package manager) can use to automatically install the correct modules at the specified version. First, you need to set up a virtual environment. If you use VSCode, the Python Environment Manager extension can automate some of this. Regardless, here are the relevant commands to use in your clone of the git repository:

```bash
#create the virtual environment
python -m venv .venv

#activate the new virtual environment
./.venv/Scripts/activate
```

After you create the environment for the first time, you only need to activate it when opening the project in the future.

Now you can install the packages listed in requirements.txt using this command:

```bash
pip install -r ./requirements.txt
```

Now the packages are installed! You shouldn't need to do this again unless we add some packages to the requirements.txt in the future. This time, you really are ready to go!

## Using git to save and share your work

Git is version control software, designed to make it easy to merge the work of several people and keep track of every change ever made. This means that (if you use the right commands) no work is ever lost, even if you delete it.

To add changed files to your local git staging area, use the following command:

```bash
git add filename
```

If you want to add everything in the current folder, use this one instead:

```bash
git add .
```

To commit your changes that you have staged from above, you use:

```bash
git commit -m "your message here"
```

Be sure to write a good commit message, because it will be visible to everyone alongside the changes you made. It should summarize the changes so that someone else can understand what you did without reading your code. For example, you might say "Added test for bad API call."

When you are ready to save all of your commits thusfar to github, use the command:

```bash
git push
```

This will put everything in your branch on the github copy of your branch. The repository manager will handle everything from there, making sure everyone's code plays nicely and nothing breaks.

If you need to get the work that someone else has pushed to github, you can use the following command:

```bash
git pull
```

## Notes on PyTest

Pytest is picky about the way you name things. Files and folders that contain tests must begin with the word 'test' which has been handled already. The tests themselves must be in classes that start with the word 'Test' as in the 'test_example.py' file. Each individual test must also start with the word 'test' which you can see in the same file. In short, if you add a test, start the name with 'test\*'.

To run PyTest, you use the following command:

```bash
pytest
```

Pretty straightforward this time, nothing fancy hiding here. We can worry about the other ways to use pytest after our test-building phase is finished.
