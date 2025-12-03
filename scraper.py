import requests
from bs4 import BeautifulSoup
import time
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# ----------------------------
# CONFIGURATION
# ----------------------------
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; WebScraper/1.0; +https://example.com/bot)"
}
RATE_LIMIT_SECONDS = 1

# Email Configuration (Load from environment variables for security)
EMAIL_SENDER = os.environ.get("EMAIL_SENDER", "your_email@gmail.com")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD", "your_app_password")
EMAIL_RECEIVER = "miamilovesgreenlandscaping@gmail.com"

# Site Configurations
SITES = [
    {
        "name": "Perfect Cut Landscaping",
        "url": "https://561lawn.com/jobs/",
        "type": "list_text", # Custom type for this site's structure
        "selector": "span.pp-list-item-text"
    },
    # Add more sites here in the future
]

# ----------------------------
# SCRAPER FUNCTIONS
# ----------------------------
def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[ERROR] Failed to fetch {url}: {e}")
        return None

def parse_site(html, site_config):
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    if site_config["type"] == "list_text":
        job_spans = soup.select(site_config["selector"])
        for span in job_spans:
            title = span.get_text(strip=True)
            # Filter out locations
            if title and ", FL" not in title and "West Lake" not in title and "Loxahatchee" not in title and "Greenacres" not in title and "Palm Springs" not in title:
                results.append({
                    "site": site_config["name"],
                    "title": title,
                    "url": site_config["url"]
                })
    
    return results

def save_to_csv(data, filename="jobs.csv"):
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["site", "title", "url"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Successfully saved {len(data)} jobs to {filename}")
    except IOError as e:
        print(f"[ERROR] Failed to save CSV: {e}")

def send_email(new_jobs):
    if not new_jobs:
        print("No new jobs to email.")
        return

    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = f"New Landscaping Jobs Found ({len(new_jobs)})"

    body = "Here are the latest landscaping jobs found:\n\n"
    for job in new_jobs:
        body += f"- {job['title']} at {job['site']}\n  Link: {job['url']}\n\n"

    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, text)
        server.quit()
        print(f"Email sent successfully to {EMAIL_RECEIVER}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        print("Make sure you have set EMAIL_SENDER and EMAIL_PASSWORD environment variables.")

# ----------------------------
# MAIN SCRIPT
# ----------------------------
def main():
    all_jobs = []
    
    for site in SITES:
        print(f"Scraping {site['name']}...")
        html = fetch_page(site['url'])
        if html:
            jobs = parse_site(html, site)
            print(f"Found {len(jobs)} jobs.")
            all_jobs.extend(jobs)
            time.sleep(RATE_LIMIT_SECONDS)

    if all_jobs:
        save_to_csv(all_jobs)
        
        # In a real scenario, you might compare with previous run to only email *new* jobs.
        # For now, we email all found jobs.
        send_email(all_jobs)
    else:
        print("No jobs found.")

if __name__ == "__main__":
    main()
