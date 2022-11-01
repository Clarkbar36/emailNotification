# Need to build out! 

### Dependent Packages:

A few packages will need to be installed in order for this function to work. First is the configparser package. This will allow the script to parse a config file. The config file will contain sensitive information as well as information to send in the email. The second is SendGrid, this the service that will be facilitating the email send. The function will utilize SendGrid's API to send out the email.

To install these packages:
```
pip install configparser
```
```
pip install sendgrid
```

### Setup Config File:

This function relies upon a config file to store pertinent information to be sent in the emails. Please see the [Example Config File](https://github.com/Clarkbar36/emailNotification/blob/master/example_config.ini) for exact layout. 

The config file should have a section for each block of code you would like to send an email for. Here are the requirements for the config file:

* section - This is the name of the email section, this will be supplied to the function so the function knows which data to pull.
* key - This is the API key for SendGrid, please reach out to Alex Clark for the key.
* to_email - This is a list of email addresses you want to receive your email. **Each email address needs to be surrounded by double quotes and separated by a comma.**
* subject - This is the subject of the email.
* success_body - This is what the body of the email should say upon a successful run.
* failure_body - This is what the body of the email should say upon a failed run.

Each section can be used to send a unique set of success/failure email.

### Implementation:
Download the [EmailFunc.py](https://github.com/Clarkbar36/emailNotification/blob/master/EmailFunc.py) file into your project directory. 

1. Go to the file on GitHub.
2. Find the button that says "raw" in the upper left-hand side of the script. 
3. Right-click on the page and click "Save-as".
4. Save as a .py file in your project directory. 

### import in traceback
### from EmailFunc import sendemail
### setup try and except
### try should have your code along with the email function
### except should have everything from exmaple

