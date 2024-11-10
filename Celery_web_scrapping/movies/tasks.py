from celery import shared_task

# To transform this function into a Celery task, all you need to do is decorate it with @shared_task
@shared_task
def add(a,b): #here we cannot use the django models instances as args 
    return a+b