# dev-activity

Auhtor:  Erin James Wills, ejw.data@gmail.com

![Continuous Integrations](./images/dev-activity-integrations.png)

<cite>Photo by <a href="https://unsplash.com/@campaign_creators?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Campaign Creators</a> on <a href="https://unsplash.com/photos/--kQ4tBklJI?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></cite>

<br>

## Overview
This repo is used to demonstrate work flow processes used in data pipelines.  Here are some examples:
* Checking for formatting and file structure issues prior to committing with git hooks:`pre-commit`
* Testing code functionality by checking input and output consistency:  `unittest` and `pytest`
* Creating custom git commands that automate common routines

## Purpose
The overall goal of this repo is very specific:  I would like to automate common routines and create a workflow of best practices.  Intially, I thought I would use two features to add workflows - git hooks by using `pre-commit` and github actions as my simple CI/CD tool.  I immediately saw three problems.  First, pre-commits are nice in concept but by default they run on all branches unless you manipulate the config file for each branch.  I would prefer to have different procedures for `bug` and `feature` branches as well as a `test` branch and a `dev` branch.  The final branch would be the `prod` branch.  The second problem is that pre-commits are locally controlled and can be modified or simply bypassed if the user desires.  The pre-commits should be used not as a policy but as a best practice before sending updates to be merged.  The third problem is that the commit failures can become annoying and discourage frequent commits for version control and pushes for backup purposes.  These realizatons helped me design the following plan as a compromise that encourages good habits and separates that from good policies:

1.  Branches for `bug` and `feat` do not have required git pre-commit rules.  Users can commit and push anything to their branch but they need to use the `git autopush` command which is a [custom command that I created for this particular scenario](./docs/custom-git.md).  This command allows for bypassing the pre-commit rules and adds a prefix to the commit message that identifies it as a `RAW` branch or a `CLEANED` branch.  The custom command simplifies the process.  The user should also know that before wanting to push code for a merge that the pre-commit program should be run.
1.  Since users will not be able to guarentee their use of pre-commits, the github actions will have a check to make sure that before a merge commit occurs to the `test` branch that the checks have been completed.
1.  After a merge to `test` has occurred then several unit tests will be deployed specific to the changes.  If those pass, then the branch is merged into `dev`
1.  After a merge to `dev` a final set of broader functionality testing occurs.
1.  The last step is to merge the `dev` into `prod` and at this phase the standard reliabilty testing occurs through synthetic and direct testing.


## GitHub Workflows
Right now these files are just proof-of-concept tests to solve initial design issues.
* `test-checks.yaml` only runs when a merge is attempted on the `test` branch.  This branch runs the pytest functionality tests.
* `python-app.yaml` only runs when a merge is attempted on the `main` branch.  This is a template workflow from github and will be customized in the future.

## Other GitHub Configurations
*  Protection from force-pushes and branch deletion was added to the `test`, `dev`, and `main` branches.

## Unit Testing Uses
* For batch data that may be applied to training on a machine learning pipeline:
    *  Check that all required columns are present for the pipeline
    *  Check for a minimum number of rows
    *  Check for data range (min/max)
    *  Check for date range
    *  Check for distribution
    *  Check for maximum execution time

## Future Work
- [x] Update names for github workflows
- [ ] Use `test-pull-request-checks.yaml` as a template for checks on the `dev` and `main` branch
- [x] Rename `main` branch to `prod`
- [x] Determine what type of configuration is needed with `pre-commit ci`.  Using default settings currently.
- [x] Create github workflow that uses `.pre-commit-config.yaml` in the `push` or `pull_request` step of the `test` branch to fix formatting.  This solves the issue if the user bypasses the `pre-commit` locally.
- [ ] Create a workflow that can automatically push changes from any branch to `test` > `dev` > `prod` assuming no errors.

## Installation
- `pip install pre-commit`
- To confirm installation, type: `pre-commit —V`


## Intitial Setup
1.  Create an initial yaml file.  This step could be done manually.
    * Type: `pre-commit sample-config > .pre-commit-config.yaml`
1.  Add any additional pre-commits as needed.  The hook can be created in this file or reference an external file url.
1.  Before this file or any changes to this file can take effect, run this command:  `pre-commit install`


## Usage
1.  Functionality is now automatically added when running `git commit -m "<message>"`

## Reference:
[pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)


Popular hook projects:
| Title | Description |
|---------------|---------------------|
| removestart |  |
| isort  | formats code |
| black  | formats python code |
| flake8  | formats code |
| mypy  |  |
| dodgy  | checks for commit passwords, secret keys, etc  |
| pylint  | formats code |
| bandit | checks for security issues |
