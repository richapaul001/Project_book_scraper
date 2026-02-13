<!DOCTYPE html>
<html>
<body>
<pre>

<h1> Book Price Tracker </h1>
<h3> Overview </h3>

Book Price Tracker is a Python-based web scraping and automation project that collects book information from an e-commerce website and stores it in a CSV file for further analysis. The project is designed with a clean, modular structure and supports automated execution via a batch file and Windows Task Scheduler.

This project demonstrates practical skills in web scraping, Python packaging, file handling, and task automation.


<h3> Tech Stack </h3>

Python

Requests – HTTP requests

BeautifulSoup – HTML parsing and scraping

CSV / File handling – Data persistence



<h3> Designed for automation (hourly execution supported)</h3>

Runs once per execution and exits cleanly



<h3> How to Run the Project </h3>

1️⃣ Run manually (one-time execution)

From the project root directory:
python -m scheduler.schedules

OR using the batch file:
run_scheduler.bat

2️⃣ Automated execution (Windows)

You can automate the project using Windows Task Scheduler.
Configure the task to run run_scheduler.bat
Set the trigger to repeat every 1 hour
The script runs once and closes automatically


<h3> Use Cases </h3>

Track book price changes over time
Build datasets for analysis or visualization
Practice real-world web scraping
Portfolio / resume project for Python roles

<h3> Future Improvements </h3>

Add logging instead of print statements
Store data in a database (SQLite/PostgreSQL)
Add price trend analysis
Notifications on price drop (email / Telegram)

👤 Author
Richa Paul Giri

</pre>
</body>
</html>
