# Contributing
This repository –whether a software project, design guide, or other, also called 'component’– can be used to convert any code into GeneXus code.

It is [licensed under Apache 2.0](./LICENSE), so all contributions must comply with this licensing.

## How can you contribute?
To be accepted, contributions must involve:
1. An incident fix (either an error correction, code enhancement or new features),
1. Improving the extensibility and/or
1. Completeness of the component.
Basically, contributions must not substantially change the existing functionality and must be useful for any of the [Globant Enterprise AI](./EnterpriseAISuite.md) components.

Contributions are accepted in the `main` branch. There are other branches defined in the repositories but no contributions will be accepted in them.

### Search for previous incidents
The first step is to review the status of incidents already reported, which helps to enhance your communication with the team responsible for the component, avoiding duplicate reporting of issues or even reporting an already corrected issue; each incident provides information about its current process status.

If the incident has been reported and its correction is pending, keep the incident number for future reference when the solution is available.

### Report an Incident 

#### Required information 
To make a good report, certain information must be included:
- Description of the issue indicating the functionality that doesn’t achieve the expected performance.
- Sample code showing the use case that doesn’t work as desired.
- About running an application using the Globant Enterprise AI API, include the following:
- Instance, Organization, Project, Assistant or component involved;
- Add the code snippet that can reproduce the case.

#### Where to make the report
Improvements to the component itself can be reported through GitHub issues, if the repository has this option enabled. This report must be submitted in English.

### Fork & Pull Request (PR)
The Fork and Pull Request (PR) mechanisms provided by GitHub are used to make a contribution.

#### Are you new to GitHub?
GitHub provides some useful guides to get started:
[Getting Started with GitHub](https://help.github.com/en/github/getting-started-with-github) there you will find how to initialize the development environment to use GitHub, as well as [how to create a Fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-forks) and [work with a Pull Request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request-from-a-fork).

#### Process
1. Create a Fork of the project on which you want to collaborate.
1. Make changes to the project in its version.
  - When the code is built without any new errors or warnings,
  - And tested, you can integrate it into the main repository.
1.	Make a PR.

This PR will be pending audit by repository managers within the organization. The result can be as follows:
- Approved, in which case the changes are integrated into the organization's repository;
- Request for improvements or changes to the PR;
- Rejected.

### Acceptance of a PR
This result depends on the next process to be carried out by those responsible for the component (failure of any of these steps will imply a possible rejection of the PR or the request for improvements to it):
1. Confirm that there is an incident associated with the PR.
1. Try to reproduce the issue in the ‘main’ branch.
1. Build and integrate the PR and check that the error obtained in the previous step has been corrected.
1. Run an integration test.
1. Check that the project’s style guidelines have been followed.
1. Approve the PR.

Some of these steps depend on good and effective communication with the team in charge. Read the next section for suggestions on the matter.

#### Requirements for a good PR
- There can be no project build errors (when you make a 'Git Checkout’ + PR build, confirm that the result is error-free).
- As for the PR comment, it should:
  - Be in English,
  - Define a title that describes the problem,
  - Include the incident number (depending on the system in which it has been reported, it will be an IT/SAC or GitHub Issue number),
  - Include additional information to help understand the need for the change and how to prove it, especially if the incident information is incomplete (review the section [Report an incident](#report-an-incident) to make sure that you have all the necessary information).
- A PR must solve a single incident.

## Scope
Accepted contributions will be available on the `main` branch.
