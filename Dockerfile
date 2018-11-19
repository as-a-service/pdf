FROM python:3

RUN apt-get update && \
	apt-get install -y \
		potrace \
        imagemagick

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip install Flask requests
CMD ["python", "trace.py"]