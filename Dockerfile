FROM grubykarol/locust:0.11.0-python3.6-alpine3.9
COPY locust_scripts /locust
ENV ATTACKED_HOST http://193.61.36.55:8000
