FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    firefox-esr \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    xdg-utils \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

RUN wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin/ \
    && rm /tmp/geckodriver.tar.gz

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

ENV DISPLAY=:99

WORKDIR /aqa-course

CMD ["tail", "-f", "/dev/null"]
