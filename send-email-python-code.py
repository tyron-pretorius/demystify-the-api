# Send one email with the Resend API from Google Colab.
# Before running: add your Resend API key in Colab Secrets (key icon in the left sidebar)
# with the name resend_api_key, and turn on Notebook access.
# Replace you@example.com with the email you signed up to Resend with.

import requests
import json
from google.colab import userdata

my_api_key = userdata.get('resend_api_key')

url = "https://api.resend.com/emails"

payload = json.dumps({
  "from": "onboarding@resend.dev",
  "to": "you@example.com",
  "subject": "My first Python API email",
  "html": "<p>I just sent this email with a Python API!</p>"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {my_api_key}'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.status_code)
print(response.text)
