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

To receive email notifications, you need to configure your credentials:

1.  **Rename** the file `.env.example` to `.env`.
2.  **Open** `.env` in a text editor.
3.  **Fill in** your details:
    - `EMAIL_SENDER`: Your Gmail address.
    - `EMAIL_PASSWORD`: Your **App Password** (not your login password).
      - [Get an App Password here](https://myaccount.google.com/apppasswords).

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
