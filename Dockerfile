# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
#ENV DJANGO_SETTINGS_MODULE news_Application.settings

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app/
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port your Django app will run on
EXPOSE 8000

# Define the command to run your Django app 
CMD ["python3", "news_Application/manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["python3", "news_Application/manage.py", "runserver", "0.0.0.0:8000"]
