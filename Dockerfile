FROM python: 3.9

WORKDIR /exercise_hub

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]