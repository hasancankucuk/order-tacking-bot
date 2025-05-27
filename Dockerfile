FROM rasa/rasa:3.6.16

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

USER root

COPY ./backend /app/backend
COPY ./backend/requirements.txt /app/requirements.txt
COPY ./backend/start.sh /app/start.sh
COPY ./backend /app

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN chmod +x /app/start.sh

EXPOSE 5000 5005

ENTRYPOINT ["/app/start.sh"]
