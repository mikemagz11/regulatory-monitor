import subprocess


def send_email(subject, body, recipients):
    """
    Send an email through Microsoft Outlook on macOS.
    recipients should be a list of email addresses.
    """

    recipient_script = ""

    for recipient in recipients:
        recipient_script += f'''
        make new recipient at newMessage with properties {{
            email address:{{address:"{recipient}"}}
        }}
        '''

    subject = subject.replace('"', '\\"')
    body = body.replace('"', '\\"')

    applescript = f'''
tell application "Microsoft Outlook"

    set newMessage to make new outgoing message with properties {{
        subject:"{subject}",
        content:"{body}"
    }}

    {recipient_script}

    send newMessage

end tell
'''

    subprocess.run(
        ["osascript", "-e", applescript],
        check=True,
    )