import traceback  # Gathers error messages to send in email
from EmailFunc import sendemail  # import module to send out emails

try:  # wrap all code in a try: statement

    # Assign a numeric value
    number = 75  # change to '75' for failure test

    # Check the is more than 70 or not
    number >= 70

    # if successful send email, put at the end of code, when you are ready to send a success email
    sendemail('SENDGRID1')

# put this code after all of your other code, this will be used to catch errors and email out a failure
except Exception as e:
    sendemail('SENDGRID1', traceback.format_exc())

try:  # wrap all code in a try: statement

    # Assign a numeric value
    number = '75'  # change to '75' for failure test

    # Check the is more than 70 or not
    number >= 70

    # if successful send email, put at the end of code, when you are ready to send a success email
    sendemail('SENDGRID2')

# put this code after all of your other code, this will be used to catch errors and email out a failure
except Exception as e:
    sendemail('SENDGRID2', traceback.format_exc())



