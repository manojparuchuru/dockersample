# Use an Alpine Linux base image
FROM alpine:latest

# Install Python
RUN apk add --update python3 py3-pip 

WORKDIR /home/data

# Copy the Python script into the container
COPY script.py IF.txt Limerick-1.txt /home/data

# Command to run the script
CMD ["python3", "script.py"]
