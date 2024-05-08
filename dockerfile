# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# This should mapped to filesystem. But incase is isn't this will prevent fail.
RUN mkdir /app/logs

# Copy the Flask application code into the container
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV NAME Python Flask Timezone Localiser

# Run app.py when the container launches
CMD ["python", "app.py"]