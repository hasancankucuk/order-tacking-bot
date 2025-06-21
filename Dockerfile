FROM rasa/rasa:3.6.16

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

USER root

COPY ./backend /app

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x start.sh

EXPOSE 5000 5005 5055

ENTRYPOINT ["./start.sh"]