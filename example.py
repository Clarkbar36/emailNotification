import configparser  # Load in library to read API Key from Config file
import traceback  # Gathers error messages to send in email
from EmailFunc import sendemail  # import module to send out emails

try:  # wrap all code in a try: statement
    config = configparser.ConfigParser()  # load parser
    # ensure config exists and can be opened, if not, it will throw an error
    try:
        with open('config.ini') as f:
            config.read_file(f)
    except IOError:
        print("config.ini not found.")
        quit()

    # Assign a numeric value
    number = '75'  # change to '75' for failure test

    # Check the is more than 70 or not
    number >= 70

    # if successful send email, put at the end of code, when you are ready to send a success email
    sendemail(config['API']['key'])

# put this code after all of your other code, this will be used to catch errors and email out a failure
except Exception as e:
    sendemail(config['API']['key'], traceback.format_exc())



