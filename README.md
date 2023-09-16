# dev-activity






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
