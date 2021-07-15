FROM python:3-alpine

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN apk add libreoffice \
	build-base \ 
	# Install fonts
	msttcorefonts-installer fontconfig && \
	# Install Calibri substitute from edge
	apk add font-crosextra-carlito --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing && \
    update-ms-fonts && \
    fc-cache -f

RUN apk add --no-cache build-base libffi libffi-dev

RUN pip install Flask requests gevent
COPY . $APP_HOME

# prevent libreoffice from querying ::1 (ipv6 ::1 is rejected until istio 1.1)
RUN mkdir -p /etc/cups && echo "ServerName 127.0.0.1" > /etc/cups/client.conf

CMD ["python", "to-pdf.py"]
