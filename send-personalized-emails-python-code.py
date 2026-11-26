# Send a personalized email to each name in a list with the Resend API from Google Colab.
# Before running: add your Resend API key in Colab Secrets (key icon in the left sidebar)
# with the name resend_api_key, and turn on Notebook access.
# Only edit your_email and names.

import requests, time
from google.colab import userdata

api_key = userdata.get("resend_api_key")   # from Colab Secrets
your_email = "you@example.com"             # the email you signed up to Resend with
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
    time.sleep(1)  # free plan: max 2 requests per second
