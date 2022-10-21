import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from http.client import responses


def sendemail(api_key, *tb: str):

    ############### User Update ###################################################
    # Must use this email address, as it's associated with SendGrid
    from_email = Email(
        "Healthlab_Software_Team@URMC.Rochester.edu")

    # Change to your recipient(s)
    to_email = [To("email_address2@domain.com")
                # ,To("email_address2@domain.com")
                # ,To("email_address3@domain.com")
                ]

    # Enter in the subject of the email, state which API/Job this is reporting on
    subject = "This is a Test"

    # Enter message to be sent upon successful run
    success_body = "We did it!"

    # Enter message to be sent upon failed run
    failure_body = "Job failed."
    ################################################################################

    # This will include the error message in your email, no need to touch
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
