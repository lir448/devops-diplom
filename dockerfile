FROM python:3.8-slim

WORKDIR /app
COPY ./covid-app /app
RUN pip install -r requirements.txt
ENV FLASK_ENV="development"
ENV FLASK_APP="covid-stats"
EXPOSE 5000
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]