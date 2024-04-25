# Use the official Python image
FROM python:3.11

# Set the working directory to /app in the container
WORKDIR /app

# Copy the Python script into the container
COPY CTF.py /app/

# Set an environment variable for the flag
ENV FLAG="SwatiCTF{You_Got_it}"

# Expose the port the app runs on
EXPOSE 200

# Run the Python script
CMD ["python", "CTF.py"]
