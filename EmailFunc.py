import configparser  # Load in library to read API Key from Config file
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from http.client import responses


def sendemail(section: str, *tb: str):
    config = configparser.ConfigParser()  # load parser
    # ensure config exists and can be opened, if not, it will throw an error
    try:
        with open('config.ini') as f:
            config.read_file(f)
    except IOError:
        print("config.ini not found.")
        quit()

    api_key = config[section]['key']

    # email address, it's associated with SendGrid
    from_email = Email("Healthlab_Software_Team@URMC.Rochester.edu")

    # parse email addresses from config file
    emails = config[section]['to_email']
    to_email = []
    for em in emails.split(","):
        make_to = To(em)
        to_email.append(make_to)

    # subject of the email from config file
    subject = config[section]['subject']

    # message to be sent upon successful run from config file
    success_body = config[section]['success_body']

    # message to be sent upon failed run from config file
    failure_body = config[section]['failure_body']

    # This will include the error message in your email
    if len(tb) == 0:
        content = Content("text/plain", success_body)
    else:
        tb = ''.join(tb)
        err_content = failure_body + "\n" + tb
        content = Content("text/plain", err_content)

    # Gather all pieces to send out
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Need to set up api key in config file
    sg = sendgrid.SendGridAPIClient(api_key=api_key)

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print("Request: " + str(responses[response.status_code]))
