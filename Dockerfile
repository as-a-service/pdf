FROM python:3-alpine

RUN apk add libreoffice \
	msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask requests
CMD ["python", "to-pdf.py"]