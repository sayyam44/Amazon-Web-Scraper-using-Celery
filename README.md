# Asynchronous Amazon Web Scraper
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
- **Django, Celery and Redis Integration**: Background tasks and scheduling for scraping.
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

## Below are some Screenshots from the project:

## List of all the periodic tasks being set for celery to schedule web scraping task and their details:
![Django Admin(Periodic Tasks) - 1](https://github.com/user-attachments/assets/a0ac7721-392d-44e0-b563-de4499004cfd)

## Details of the product being scrapped on Django Admin:
![Django Admin-One of the Product Scraped event - 2](https://github.com/user-attachments/assets/d0ef9c2a-2096-4c4e-a458-84ccbe52254d)

## List of few Product Scraped events being created by celery at the backend:
![Django Admin - Product Scraped events created - 3](https://github.com/user-attachments/assets/de9624c1-6027-4d25-bd5f-a7c1cf6a824b)

## Event Scheduler i.e. Celery beat running in terminal running scrapping tasks
![5](https://github.com/user-attachments/assets/7acb8579-6276-495d-b967-9fbb4711a6c9)

## Reference - 
https://realpython.com/asynchronous-tasks-with-django-and-celery/#python-celery-basics

Thanks!
