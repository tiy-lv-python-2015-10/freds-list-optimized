# Fred's List Evolved

## Description
While the original Fred's List works it still needs many enhancements.  Its original counterpart 
in real life has no api and this needs to rectified.  Additionally, more features will be needed
to round out the system

## Objectives
* Integrate with a functioning full 3rd party api
* Create an API to suppliment an existing system
* Use token authentication to allow users to post and update data into a system

## Details

### Deliverables
* Pull request for django project

### Requirements
* Tests for API calls
* Implement all features from Normal Mode
* No pep8 errors
* No systems files checked in

## Normal Mode

### New features
* Create a Best Of feature that show the top 50 most favorited posts in the past week
* On the user account page display the current api token for the user as well as a button to regenerate it
* Create a notification feature that will allow users to:
	* Add/Remove notifications based on keywords to look for in title and description
	* Will use signals to send a notification when a new post is updated with the search criteria
* Create a search feature on the post list page that will search the title and description for any posts containing the words
* Implement Sendgrid to handle all outgoing transactional emails

### API
* Implement a restful api using Django Rest Framework for all models in the system.
* Ensure that users can only update and edit their own information
* Use filters with the api to implement the search feature on the post list
* Add endpoint that will display the top50 feature as described above

### Sendgrid
This is a transactional email sender that will provide detailed reporting on emails sent.  To get going:
* Sign up for an account (it's free)
* Click your name drop down on the dashboard
* Look for the API keys option
* Add a new key (Don't forget to copy it down)
* Now read through the documentation for your options:
	* Official SendGrid Python Library: https://github.com/sendgrid/sendgrid-python#example
	* DJango Library: https://github.com/elbuo8/sendgrid-django
	* WebV2 API: https://sendgrid.com/docs/API_Reference/Web_API/index.html
