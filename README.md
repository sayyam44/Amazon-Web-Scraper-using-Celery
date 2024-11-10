# Amazon Web Scraper Using Celery
This project demonstrates how to schedule web scrapping tasks using Celery to track Amazon product price fluctuations. It leverages Celery for scheduling background tasks, Selenium and BeautifulSoup for web scraping, and Django for efficient data storage.

## What is Celery ?
Celery is a distributed task queue that allows you to offload, manage, and execute tasks asynchronously outside of your main application.

## why Redis or RabbitMQ ?
Celery requires a message broker to receive tasks and send results to the backend. Redis and RabbitMQ are commonly used message brokers in Celery setups.

## Why Use Celery?
There are two primary reasons developers turn to Celery:

1) To offload tasks from the main application, enabling them to run independently in distributed processes.
2) To schedule tasks to run at specific times or on a recurring basis.
   
While both functionalities are part of Celery, they are typically addressed separately:
-->Celery workers are independent processes that execute tasks outside the main service.
-->Celery Beat is a scheduler that handles when tasks should run, including periodic task execution.


## Features
- **Django & Celery Integration**: Background tasks and scheduling for scraping.
- **Selenium Automation**: Automates browser actions and scrapes data from Amazon.
- **Bright Data (formerly Luminati)**: Advanced proxy scraping techniques to handle Captchas and IP bans.
- **Data Parsing**: Extract relevant product details (like price) using BeautifulSoup4.
- **Django Models**: Efficiently store scraped data in structured models.
- **Scheduled Scraping**: Automate and schedule scraping tasks through the Django admin using Celery.

