# Contributing to plane-alert-db

We love your input! 🚀 We want to make contributing to this project as easy and transparent as possible, whether it's:

-   [Reporting a bug](https://github.com/sdr-enthusiasts/plane-alert-db/issues/new?assignees=&labels=bug&template=bug_report.yml).
-   Discussing the current state of the code.
-   [Submitting a fix](https://github.com/sdr-enthusiasts/plane-alert-db/compare).
-   [Proposing new features](https://github.com/sdr-enthusiasts/plane-alert-db/issues/new?assignees=&labels=enhancement&template=feature_request.yml).
-   [Reviewing pull requests](https://github.com/sdr-enthusiasts/plane-alert-db/pulls).
-   Adding new planes or images.
-   Becoming a maintainer.

## We Develop with Github

We use github to host code, track issues and feature requests, and accept pull requests.

## We Use [Github Flow](https://guides.github.com/introduction/flow/index.html), So All Code Changes Happen Through Pull Requests

Pull requests are the best way to propose changes to the codebase (we use [Github Flow](https://docs.github.com/en/get-started/quickstart/github-flow)). We actively welcome your pull requests:

1.  Fork the repo and create your branch from `main`.
2.  Create a new feature branch to implement your changes on.
3.  Add tests if you've added code that should be tested.
4.  If you've changed the internal working of the repository, update the documentation.
5.  Ensure the test suite passes.
6.  Make sure your code lints.
7.  Issue that pull request!

## Keep your fork updated

As the [README](README.md) explains, this repository uses GitHub actions to create several derivative databases from the main databases. By default, the [create_db_derivatives.yaml](.github/workflows/create_db_derivatives.yaml) action is disabled on forks. You, therefore, have to Set the `CREATE_DERIVATIVES` repository variable to `true` in your repository settings (see [the GitHub documentation](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-a-repository)) if you want this action to generate the correct derivative databases on your fork automatically

## Report bugs using Github's [issues](https://github.com/sdr-enthusiasts/plane-alert-db/issues)

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/sdr-enthusiasts/plane-alert-db/issues/new/choose); it's that easy!

## Write bug reports with detail, background, and sample code

[This is an example](http://stackoverflow.com/q/12488905/180626) of a bug report, and I think it's a good model. Here's [another example from Craig Hockenberry](http://www.openradar.me/11905408), an app developer greatly respected in the community.

**Great Bug Reports** tend to have:

-   A quick summary and/or background.
-   Steps to reproduce:
    -   Be specific!
    -   Give sample code if you can. [A stackoverflow question](http://stackoverflow.com/q/12488905/180626) includes sample code that _anyone_ with a base R setup can run to reproduce the error.
-   What you expected would happen
-   What actually happens.
-   Notes (possibly including why you think this might be happening, or stuff you tried that didn't work).

People _love_ thorough bug reports. I'm not even kidding.

## Use a Consistent Coding Style

We use [black](https://github.com/psf/black) formatter to format our python code. You are advised to use [flake8](https://flake8.pycqa.org/en/latest/) for linting your code.

## References

This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/a9316a723f9e918afde44dea68b5f9f39b7d9b00/CONTRIBUTING.md).
