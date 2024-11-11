# Amazon Web Scraper Using Celery
This project demonstrates how to schedule web scrapping tasks using Celery to track Amazon product price fluctuations. It leverages Celery for scheduling background tasks, Selenium and BeautifulSoup for web scraping, and Django for efficient data storage.

## What is Celery ?
Celery is a distributed task queue that allows you to offload, manage, and execute tasks asynchronously outside of your main application.

## Why Redis or RabbitMQ ?
Celery requires a message broker to receive tasks and send results to the backend. Redis and RabbitMQ are commonly used message brokers in Celery setups.

## Why Use Celery?
There are two primary reasons developers turn to Celery:

1) To offload tasks from the main application, enabling them to run independently in distributed processes.
2) To schedule tasks to run at specific times or on a recurring basis.
   
While both functionalities are part of Celery, they are typically addressed separately:
### Celery workers are independent processes that execute tasks outside the main service.
### Celery Beat is a scheduler that handles when tasks should run, including periodic task execution.


## Features
- **Django & Celery Integration**: Background tasks and scheduling for scraping.
- **Selenium Automation**: Automates browser actions and scrapes data from Amazon.
- **Data Parsing**: Extract relevant product details (like price) using BeautifulSoup4.
- **Django Models**: Efficiently store scraped data in structured models.
- **Scheduled Scraping**: Automate and schedule scraping tasks through the Django admin using Celery.

## Steps to Set Up and Run the Project
### 1. Clone the repository :
   ```bash
   git clone https://github.com/sayyam44/Amazon-Web-Scraper-using-Celery.git
   ```
   
### 2.Install required packages: Navigate to the project directory and install the dependencies:
```bash
   pip install -r requirements.txt
```

### 3. Run a Local Redis Instance via Docker Compose
If you’re using Redis as the message broker, start a local Redis instance with Docker Compose:
```bash
   docker compose -f compose.yaml up -d
```
### 4.Run the server using:
```bash
   python manage.py runserver
```

### 5. Start the Celery Worker and Beat
In separate terminals, run the following commands:
```bash
   celery -A Celery_web_scrapping2 worker --pool=solo -l info
```
```bash
   celery -A Celery_web_scrapping2 beat --loglevel=info
```
### 6. Add a New Periodic Task in Django Admin
As soon as you add a new periodic task in the Django admin panel, you will see the schedule change reflected in the Celery Beat terminal and hence data being saved and updated into the Django models on the basis of the defined time of the Celery event .
