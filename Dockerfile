# Use the official Python image as the base image
FROM python:3.12-slim

# Install Chrome and ChromeDriver
RUN apt-get update && \
    apt-get install -y wget unzip \
                       libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
                       libxss1 libxtst6 libnss3 libgdk-pixbuf2.0-0 \
                       libglib2.0-0 libatk-bridge2.0-0 libgtk-3-0 && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y && \
    rm google-chrome-stable_current_amd64.deb && \
    wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip && \
    google-chrome --version && \
    chromedriver --version

# Set up working directory
WORKDIR /app

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Run tests
CMD ["pytest", "--html=reports/test_report.html", "--self-contained-html"]
