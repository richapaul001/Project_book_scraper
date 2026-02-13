<!DOCTYPE html>
<html>
<body>
<pre>
📚 Book Price Tracker
📌 Overview

Book Price Tracker is a Python-based web scraping and automation project that collects book information from an e-commerce website and stores it in a CSV file for further analysis. The project is designed with a clean, modular structure and supports automated execution via a batch file and Windows Task Scheduler.

This project demonstrates practical skills in web scraping, Python packaging, file handling, and task automation.

🗂 Project Structure
Project/
│
├── data/
│   └── books.csv            # Output CSV containing scraped book data
│
├── scheduler/
│   ├── __pycache__/
│   └── schedules.py         # Script that runs the scraping job once
│
├── scraper/
│   ├── __pycache__/
│   ├── __main__.py          # Entry point for running the scraper as a package
│   ├── config.py            # Configuration values (URLs, headers, etc.)
│   ├── csv_data.py          # CSV read/write helper functions
│   └── scrape.py            # Core web scraping logic
│
├── run_scheduler.bat        # Batch file to run the project
├── readme.md                # Project documentation
└── desktop.ini              # System file (can be ignored)


🛠 Tech Stack

Python

Requests – HTTP requests

BeautifulSoup – HTML parsing and scraping

CSV / File handling – Data persistence


✨ Features

🔄 Multi-page book data scraping

🧩 Modular and maintainable project structure

💾 CSV-based data storage


⏱ Designed for automation (hourly execution supported)

▶ Runs once per execution and exits cleanly


▶️ How to Run the Project

1️⃣ Run manually (one-time execution)

From the project root directory:
python -m scheduler.schedules

OR using the batch file:
run_scheduler.bat

2️⃣ Automated execution (Windows)

You can automate the project using Windows Task Scheduler:
Configure the task to run run_scheduler.bat
Set the trigger to repeat every 1 hour
The script runs once and closes automatically


📈 Use Cases

Track book price changes over time
Build datasets for analysis or visualization
Practice real-world web scraping
Portfolio / resume project for Python roles

🚀 Future Improvements

Add logging instead of print statements
Store data in a database (SQLite/PostgreSQL)
Add price trend analysis
Notifications on price drop (email / Telegram)
Dockerize the application

👤 Author
Richa Paul Giri

</pre>
</body>
</html>
