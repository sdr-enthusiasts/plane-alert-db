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
2.  Create a new feature branch (e.g. `patch`) to implement your changes on.
3.  Make your changes.
4.  Add tests if you've added code that should be tested.
5.  If you've changed the internal working of the repository, update the documentation.
6.  Ensure the test suite passes.
7.  Make sure your code lints.
8.  Issue that pull request!
9.  Merge your feature branch into your own `main` branch, so you don't have to wait for the PR to be merged.

## Important Development Notes

### Database Updates

Refer to the [README](README.md) for details on contributing to the following main databases:

-   [plane-alert-db.csv](plane-alert-db.csv)
-   [plane-alert-pia.csv](plane-alert-pia.csv)
-   [plane-alert-ukraine.csv](plane-alert-ukraine.csv)
-   [plane_images.csv](plane_images.csv)

Please note that other databases are automatically generated via [GitHub Actions](https://github.com/sdr-enthusiasts/plane-alert-db/actions/workflows/create_db_derivatives.yaml) and should not be manually edited.

### Readme Update

The readme is dynamically generated through the [update_readme.yml](https://github.com/sdr-enthusiasts/plane-alert-db/actions/workflows/update_readme.yml) action using the mustache template language and the chevron parser. For any modifications, exclusively edit the [readme.mustache](readme.mustache) file.

## Keep your fork up to date

You can keep your fork, and thus your private Vercel instance up to date with the upstream using GitHubs' [Sync Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) button. You can also use the [pull](https://github.com/wei/pull) package created by [@wei](https://github.com/wei) to automate this process.

## Automatically create the derivative databases

As the [README](README.md) explains, this repository uses GitHub actions to create several derivative databases from the main databases. By default, to prevent conflicts, the [create_db_derivatives.yaml](.github/workflows/create_db_derivatives.yaml) action is disabled on forks. You can, however, set the `CREATE_DERIVATIVES` repository variable to `true` in your repository settings (see [the GitHub documentation](https://docs.github.com/en/actions/learn-github-actions/variables#creating-configuration-variables-for-a-repository)) if you want to create the derivative database on your fork automatically.

> **Warning**
> If you enable the building of the derivative databases on your fork, please use a feature branch (e.g. `patch`) when creating pull requests to the main repository. This will prevent your PR from being flagged as `invalid` since commits made by the [create_db_derivatives.yaml](.github/workflows/create_db_derivatives.yaml) do not re-trigger the PR check actions. You can then merge your changes into your main branch without waiting for the PR to be merged.

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
