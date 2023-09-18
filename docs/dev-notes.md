# Development Notes
Place to put random content until I incorporate it fully into the project.

Ref:  https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/

Ref:  https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#testing-with-pytest-and-pytest-cov



**Run Pre-Commit Hook before Merge**
```bash
[hooks]
pre-commit = !sh -c 'if [[ $GIT_MERGE_HEAD ]]; then npm run pre-commit-on-merge; fi'
```
