# Landscaping Job Scraper

This tool scrapes job listings from **Perfect Cut Landscaping (561lawn.com)** and saves them to a CSV file.

## Prerequisites

- Python 3.x installed
- Internet connection

## Installation

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```powershell
   cd C:\Users\futur\.gemini\antigravity\scratch\landscaping_scraper
   ```
3. Install the required Python packages:
   ```powershell
   pip install -r requirements.txt
   ```

## Email Notification Setup

To receive email notifications, you need to set up the following environment variables:

1.  **EMAIL_SENDER**: The Gmail address you want to send emails *from*.
2.  **EMAIL_PASSWORD**: An **App Password** for that Gmail account (not your regular password).
    - Go to [Google Account Security](https://myaccount.google.com/security).
    - Enable 2-Step Verification.
    - Search for "App Passwords" and create one for this script.

### Setting Environment Variables (PowerShell)

```powershell
$env:EMAIL_SENDER = "your_email@gmail.com"
$env:EMAIL_PASSWORD = "your_app_password"
```

Then run the script:

```powershell
python scraper.py
```

## Usage

Run the scraper script:

```powershell
python scraper.py
```

## Output

- `jobs.csv`: Contains the job titles and URLs.
- Email notification sent to `miamilovesgreenlandscaping@gmail.com`.
