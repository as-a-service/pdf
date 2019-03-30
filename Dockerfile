FROM python:3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apk add libreoffice \
	msttcorefonts-installer fontconfig && \
    update-ms-fonts && \
    fc-cache -f

RUN pip install Flask requests
COPY . $APP_HOME

CMD ["python", "to-pdf.py"]