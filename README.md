# Example package

This repository is designed to demonstrate how to create a Python package which can be installed locally as a package accessible anywhere on your computer. The package consists of a series of simple functions which each have accompanying tests. These tests are used to ensure the code works as expected and that future changes of the cosebase do not break previous implementations. The tests are executed by GitHub every time someone makes a Pull Request, and on every commit to the main branch. This allows users to check the tests in a sandbox environment on GitHub servers before merging changes in the main branch.

## Creating an installable Python package

For developing packages of Python scripts where functions and classes are separated into different files and imported across scripts, it is good practice to make the scripts into a package which can be installed after downloading the source code. To do this, there are several stages.

1. Order the code into a standard layout. There are various possible configurations of code which can be used to create a Python package. In this example, we use the layout as follows:

```
.
├── [package name]
│   └── __init__.py
│   └── ...   
├── tests/
│   └── ...
├── requirements.txt
├── setup.py
```

2. Create a `requirements.txt` file which lists all the relevant packages which must be installed, and their relevant versions, in order for this package to work.

3. Create a `setup.py` file which tells the installer what to install and how to install the package. More information on the creation of this file can be found [here](https://setuptools.pypa.io/en/latest/userguide/quickstart.html).

4. Install the package locally using:

```
pip install -e .
```

Here, the `-e` flag means that the package is editable, i.e. you don't have to reinstall the package locally each time you make an edit.

**Note:** We will discuss the `tests/` folder in the next section.

## Tests



## Workflow

The workflow of this repository is a 'Feature Branch Workflow' which means that all features added/changed in the codebase are developed on a separate branch. This branch should be named descriptively such that other users know what each branch is for. A new branch is created from the main branch and moved to through:

```
git branch dev_[descriptive name]
git checkout dev_[descriptive name]
```

Once the feature has been successfully developed then it can be merged back into the main branch. This is done through pushing the branch back up to the remote repository on GitHub. The first time this is done for a new local branch the new branch must be added to the remote repository by:

```
git push --set-upstream origin dev_[descriptive name]
```

After which all subsequent pushes to the remote branch can be done through the normal `git push`.

Once the remote branch is created, it can be pulled into the main branch through using GitHub's Pull Request (PR) feature. For major changes, all PRs should have a reviewer assigned to ensure that another user has checked over the changed. It is good practice to assign a reviewer who is the most knowledeable about the given section of code changed. For simple PRs a reviewer may not be deemed necessary.

Once the PR has been approved, it can be merged into the main branch and the remote branch deleted. This deletion of the branch is good practice to ensure a clean set of branches on the remote repository. If more development is being conducted on this branch locally, deleting the remote branch will not delete the local branch and so you can continue developing there.



