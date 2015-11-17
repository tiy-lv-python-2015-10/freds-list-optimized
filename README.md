# Fred's List Optmization

## Description
It is time to make Fred's List a little more optimized and proactive with automated testing, caching and CORS

## Learning Objectives
* Understand Travis CI testing
* Be able to add CORS headers to allow remote access to API
* Effectively use caching to make expensive calls quicker

## Details

### Deliverable
* Pull request to the repository with the requirements met

### Normal Mode
* You must test have at least 1 test per html view and 1 test per api/verb combo (so both list and create)
* You must pass all tests
* Setup Travis-CI on your own fork.  It should test anything pushed to the master branch
* Your master branch README should include the travis icon indicating the branch is passing
* Cache the 50 top posts view to speed it up
* Cache at least one set of categories at a template level
* Add CORS headers to allow any host remote access to the api

### Hard Mode
* Use coverage and coveralls and have 75% code coverage
