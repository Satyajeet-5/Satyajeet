# Use the official Python image
FROM python:3.9  

# Set the working directory inside the container
WORKDIR /app  

# Copy project files into the container
COPY . /app  

# Install dependencies
RUN pip install -r requirements.txt  

# Expose the port Render assigns
EXPOSE 10000  

# Run Flask app
CMD ["python", "app.py"]
