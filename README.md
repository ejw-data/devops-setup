# dev-activity

This repo is used to demonstrate work flow processes used in data pipelines.  Here are some examples:
* Checking for formatting and file structure issues prior to committing with git hooks:`pre-commit`
* Testing code functionality by checking input and output consistency:  `unittest` and `pytest`

## Unit Testing Uses
* For batch data that may be applied to training on a machine learning pipeline:
    *  Check that all required columns are present for the pipeline
    *  Check for a minimum number of rows
    *  Check for data range (min/max)
    *  Check for date range
    *  Check for distribution
    *  Check for maximum execution time



Ref:  https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/

Ref:  https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#testing-with-pytest-and-pytest-cov


**Run Hook before Merge**
```bash
[hooks]
pre-commit = !sh -c 'if [[ $GIT_MERGE_HEAD ]]; then npm run pre-commit-on-merge; fi'
```

## Installation
- `pip install pre-commit`
- To confirm installation, type: `pre-commit —V`


## Intiial Setup
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
