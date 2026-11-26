# Demystify the API

Code and request bodies from [The Workflow Pro's Demystify the API crash course](https://theworkflowpro.com/demystify-the-api/).

## Slides
- `demystify-the-api-slides.pdf`: the full course slide deck (all 8 lessons) as a PDF.

## Making your first POST request (Postman)
- `jsonplaceholder-post-request-body.json`: the practice POST to `https://jsonplaceholder.typicode.com/posts` (no API key needed).
- `send-email-post-request-body.json`: the email you send with a POST to `https://api.resend.com/emails`. In Postman, set Authorization to **Bearer Token** with your Resend API key, then paste this into **Body → raw → JSON** and change `to` to the email you signed up to Resend with.

## Making requests in code (Python in Google Colab)
- `demystify-the-api-requests-in-code.ipynb`: both examples as a Colab notebook. Open [Google Colab](https://colab.research.google.com/), then **File → Upload notebook**.
- `send-email-python-code.py`: send one email (the code exported from Postman).
- `send-personalized-emails-python-code.py`: loop through a list of names and send each one a personalized email.
- `send-personalized-emails-anywhere.py`: the same loop for running outside Colab (see below).

Your API key goes in **Colab Secrets** (the key icon in the left sidebar) with the name `resend_api_key`, never in the code.

## No Google account? Two other ways to run the code

Use `send-personalized-emails-anywhere.py`. It's the same code as the lesson, but instead of Colab Secrets it asks you to paste your Resend API key when it runs, so your key never goes in the code.

### Option 1: in your browser with GitHub Codespaces (free)
1. Create a free [GitHub account](https://github.com/signup) if you don't have one. No Google account needed.
2. Open **[codespaces.new/tyron-pretorius/demystify-the-api](https://codespaces.new/tyron-pretorius/demystify-the-api)** and click **Create codespace**. It takes about a minute to start.
3. If VS Code asks **"Do you trust the authors of the files in this folder?"**, click **Trust Folder & Continue**.
4. Click `send-personalized-emails-anywhere.py` in the file list on the left. Change `your_email` to the email you signed up to Resend with (and the names, if you like), then save with **Cmd+S** (Mac) or **Ctrl+S** (Windows).
5. In the **Terminal** at the bottom (if it's hidden: menu ☰ → **Terminal → New Terminal**), type this and press Enter:
   ```
   python3 send-personalized-emails-anywhere.py
   ```
6. Paste your Resend API key when asked and press Enter. Nothing shows while you paste; that's normal. You should see `200` next to each name, and the emails land in your inbox.
7. When you're done, go to [github.com/codespaces](https://github.com/codespaces), click **⋯** next to your codespace and choose **Delete** (or **Stop codespace** to come back later). Free accounts get about 60 hours a month, and an idle codespace stops itself after 30 minutes.

Python and the `requests` library come pre-installed in Codespaces, so there's nothing to set up.

### Option 2: on your own computer
1. Install Python from [python.org/downloads](https://www.python.org/downloads/). On Windows, tick **"Add python.exe to PATH"** in the installer.
2. Install the `requests` library. Open Terminal (Mac) or Command Prompt (Windows) and run:
   - Mac: `python3 -m pip install requests`
   - Windows: `py -m pip install requests`
3. Download this repository (green **Code** button → **Download ZIP**) and unzip it.
4. Open `send-personalized-emails-anywhere.py` in any text editor, change `your_email` (and the names) and save.
5. Open a terminal in the unzipped folder (Mac: right-click the folder → **New Terminal at Folder**; Windows: open the folder, type `cmd` in the address bar and press Enter), then run:
   - Mac: `python3 send-personalized-emails-anywhere.py`
   - Windows: `py send-personalized-emails-anywhere.py`
6. Paste your Resend API key when asked and press Enter.

**Tip:** if you'd rather not paste the key every time, save it as an environment variable named `RESEND_API_KEY` and the script will pick it up automatically.
