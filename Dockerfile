# Use an official Python runtime as a parent image
FROM python:3

ENV PYTHONUNBUFFERED=1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Expose the port the app runs on
EXPOSE 8000

# Set up the entry point command
CMD ["bash", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:$PORT"]
