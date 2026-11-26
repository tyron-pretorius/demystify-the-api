# Send a personalized email to each name in a list with the Resend API.
# The same code as the lesson, but it runs anywhere: GitHub Codespaces,
# your own computer, or Google Colab.
#
# Only edit your_email and names, then run:  python3 send-personalized-emails-anywhere.py
# When it asks for your Resend API key, paste it and press Enter.
# (Nothing shows on screen while you paste. That's normal, it keeps your key hidden.)

import os, time
import requests


def get_api_key():
    # 1. Google Colab: a secret named resend_api_key (the key icon in the left sidebar)
    try:
        from google.colab import userdata
        return userdata.get("resend_api_key")
    except ImportError:
        pass
    # 2. An environment variable or Codespaces secret named RESEND_API_KEY
    if os.environ.get("RESEND_API_KEY"):
        return os.environ["RESEND_API_KEY"]
    # 3. Otherwise, paste it when asked (it isn't shown or saved anywhere)
    from getpass import getpass
    return getpass("Paste your Resend API key and press Enter: ")


api_key = get_api_key()
your_email = "you@example.com"   # the email you signed up to Resend with
names = ["Anna", "Ben", "Chloe"]

url = "https://api.resend.com/emails"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

for name in names:
    payload = {
        "from": "onboarding@resend.dev",
        "to": your_email,
        "subject": f"Hi {name}, this email came from Python",
        "html": f"<p>Hey {name}, I just sent this with the Resend API!</p>",
    }
    response = requests.post(url, json=payload, headers=headers)
    print(name, response.status_code, response.text)
    time.sleep(1)  # Resend's free plan allows 2 requests per second
