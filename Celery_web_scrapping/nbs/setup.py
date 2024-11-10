import os
import sys

def init_django(project_name='Celery_web_scrapping2'):
    # Get the root directory of the project (Celery_web_scrapping)
    PWD = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    print(f"Initial Working Directory (PWD): {PWD}")

    # Change to the Django project root
    os.chdir(PWD)
    print(f"Resolved Django Root Directory Path (PWD): {PWD}")

    # Update the Python path to include the project folder
    sys.path.insert(0, PWD)
    print(f"Python path after inserting PWD: {sys.path}")

    # Set the DJANGO_SETTINGS_MODULE to point to the correct settings module
    os.environ["DJANGO_SETTINGS_MODULE"] = f"{project_name}.settings"
    print(f"DJANGO_SETTINGS_MODULE: {os.environ['DJANGO_SETTINGS_MODULE']}")

    # Initialize Django
    import django
    django.setup()
    print("Django setup completed")
