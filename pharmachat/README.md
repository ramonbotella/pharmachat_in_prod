# pharmachat

[![Release](https://img.shields.io/github/v/release/ramonbotella/pharmachat)](https://img.shields.io/github/v/release/ramonbotella/pharmachat)
[![Build status](https://img.shields.io/github/actions/workflow/status/ramonbotella/pharmachat/main.yml?branch=main)](https://github.com/ramonbotella/pharmachat/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/ramonbotella/pharmachat/branch/main/graph/badge.svg)](https://codecov.io/gh/ramonbotella/pharmachat)
[![Commit activity](https://img.shields.io/github/commit-activity/m/ramonbotella/pharmachat)](https://img.shields.io/github/commit-activity/m/ramonbotella/pharmachat)
[![License](https://img.shields.io/github/license/ramonbotella/pharmachat)](https://img.shields.io/github/license/ramonbotella/pharmachat)

A package to create an AI assintant whit pharmaceutical leaflets knowledge

- **Github repository**: <https://github.com/ramonbotella/pharmachat_in_prod/>

## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:ramonbotella/pharmachat_in_prod.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).
