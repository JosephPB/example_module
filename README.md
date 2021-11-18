# Example package

This repository is designed to demonstrate how to create a Python package which can be installed locally as a package accessible anywhere on your computer. The package consists of a series of simple functions which each have accompanying tests. These tests are used to ensure the code works as expected and that future changes of the codebase do not break previous implementations. The tests are executed by GitHub every time someone makes a Pull Request, and on every commit to the main branch. This allows users to check the tests in a sandbox environment on GitHub servers before merging changes in the main branch.

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

The best ways to lay out packages can be debated with an interesting explanation for slightly changing the above layout presented [here](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure).

## Tests

Tests are used to check that all code written is executing properly. There are several ways to write tests, and various packages to help you automate testing. In this repository we use the [`pytest`](https://docs.pytest.org/en/6.2.x/contents.html) package.

Here, we separate tests in to a dedicated folder so that we don't clog up our module scripts. In this folder are files named following the convention `test_[...].py`. Inside these scripts are functions which test functions in the package. By convention, we try to have at least one test function for each package function, however, functions and their tests can be mixed to test additional complexity at the expense of potentially explainable results.

An example of a test function set up is as follows:

```
def test_[some function]:
   # code to set up and call function
   assert [function to test](args, **kwargs) == [specific result]
```

To run the tests locally, simply run `pytest` in the base directory of the package and the pytest will automatically look into the `test/` folder and run all functions beginning with `test_` in the scripts contained in this folder.

Ideally, all lines of code in a package should be testable, and have tests written for them. Therefore, whenever new functions are added to the package, or existing functions edited, corresponding tests should be added and changed accordingly to ensure maximum coverage of tests.

The above is a very simple example for a deterministic output. Tests can become increasingly sophisticated, including the adding of sythetic data, sharing modules and functions between tests, and grouping similar tests into classes. More information on these can be found on the [pytest](https://docs.pytest.org/en/6.2.x/contents.html) webpage.

Similarly, there is also a set of [Pytest conventions and good practices](https://docs.pytest.org/en/6.2.x/goodpractices.html) listed in the online documentation.

- Examples of some more complex test suites can be found [here](https://github.com/UNGlobalPulse/UNGP-settlement-modelling/tree/master/test_camps) and [here](https://github.com/IDAS-Durham/JUNE/tree/master/test_june)
- An example of tests using synthetic data can be found [here](https://github.com/JosephPB/n3jet/tree/master/tests) with `conftest.py` script containing such data.

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

Once the remote branch is created, it can be pulled into the main branch through using GitHub's Pull Request (PR) feature. For major changes, all PRs should have a reviewer assigned to ensure that another user has checked over the change. It is good practice to assign a reviewer who is the most knowledeable about the given section of code changed. For simple PRs a reviewer may not be deemed necessary.

Once the PR has been approved, it can be merged into the main branch and the remote branch deleted. This deletion of the branch is good practice to ensure a clean set of branches on the remote repository. If more development is being conducted on this branch locally, deleting the remote branch will not delete the local branch and so you can continue developing there.

## GitHub Actions

[GitHub Actions](https://github.com/features/actions) are a powerful set of tools which allow users to automate various components of software workflows. Here, we use them to automatically run the tests in the `tests/` folder in a sandbox environment setup on GitHub's servers. A fresh environment is set up by GitHub everytime the automation pipeline is run which happens every time a user commits to the main branch, and each time a PR is made. A 'successful' PR is one which has passed all the tests, and, if necesssary, been reviewed by a reviewer, and can then be merged in the main branch.

An overview of setting up a simple `.yaml` file for `pytest'ing can be found [here](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions).

The GitHub Actions are controlled by the files contained in the `.github/workflows/` folder. Here, we have a file `python-publish.yaml`. This file tells GitHub how to set up the relevant Python environment, which dependencies to install, and then runs the tests.

Example syntax's for GitHub Actions workflows can be found [here](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions) with more documentation [here](https://docs.github.com/en/actions/learn-github-actions/workflow-syntax-for-github-actions).
