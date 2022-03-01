<!--
SPDX-FileCopyrightText: 2017-2022 Contributors to the prognoses_monitoring_reports_code project

SPDX-License-Identifier: Apache-2.0
-->

# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change. 

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Style guide

This project uses the PEP 8 Style Guide for Python Code. For all details about the various conventions please refer to:

[PEP 8](https://www.python.org/dev/peps/pep-0008)

Furthermore the following conventions apply:

* Maximum line length: 88 characters
* Double quotes for strings, keys etc.
    * Except when double quotes in the middle of a string are required.

## Git branching

This project uses the [Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) and branching model. The `master` branch always contains the latest release, after a release is made new feature branches are branched of `develop`. When a feature is finished it is merged back into `develop`. At the end of a sprint `develop` is merged back into `master` or (optional) into a `release` branch first before it is merged into `master`.

This project also uses [Jira](https://www.atlassian.com/software/jira) for its [Scrum](https://en.wikipedia.org/wiki/Scrum_(software_development) planning. In order to connect git branches to Jira it is required that the user story `id` (e.g. KTP-753) is added to the branch name. The following convention will be used for feature branches: `feature-KTP-###-<descripttion>`. So for example: `feature-KTP-753-unittest-all-schedulers`.

![Gtiflow](img/gitflow.svg)

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a 
   build.
2. Update the README.md with details of changes to the interface, this includes new environment 
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you 
   do not have permission to do that, you may request the second reviewer to merge it for you.
