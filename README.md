FiveAI Practical
----------------

Welcome to the FiveAI practical. Thanks for taking the time to complete it. We
suggest that you spend one hour. It is not expected for you to complete all
the tasks.

Once you have finished the tasks chosen or have have reached a point in which
you have spent enough time on the practical, please push up your commits for
the team to review.

## Repo contents
* ./giphy-service - dir containing the python src to be hosted hosted in container
* ./README.md     - Documentation for this practical test

## Tickets:

### P-1: Dockerise the python application
Take the application found in the *giphy-service* directory and containerise it.

You may make any amendments to the source code and its dependencies to support
this process

*Requiments:*
* provide docker image file

*Expectations:*
* final image should be built to be production standards

### P-2: Setup local development environment
Using a preferred tool (docker-compose, swarm, kubernetes, etc..) provide files
which can be run locally to bring up the image.

You may make any amendments to the source code and its dependencies to support
this process

*Requirements:*
* config files and documentation to bring up the development environment

### P-3: Health check
Add a health check which can be used in a production environment to ensure
service is healthy.

Can be in the form of a script used with monitoring tools (i.e. nagios. consul)
or any other method matching your implementation.

*Requirements:*
* script or config for health check to be run against the python giphy service
