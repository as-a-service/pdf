FROM python:3

RUN apt-get update && \
	apt-get install -y \
		libreoffice

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask requests
CMD ["python", "to-pdf.py"]