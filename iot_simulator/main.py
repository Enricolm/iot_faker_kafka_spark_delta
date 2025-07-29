import random
from faker import Faker
from fastapi import FastAPI
from datetime import datetime,time

app = FastAPI()
faker = Faker()

@app.get("/iot-data")
def get_data():

    data_fixa = datetime(2025, 7, 27)

    data = {
        "device_id": faker.uuid4(),
        "temperature": round(random.uniform(4.0, 45.0), 2),
        "humidity": round(random.uniform(40.0, 90.0), 2),
        "date": faker.date_time_between(
                start_date= datetime.combine(data_fixa.date(), time.min), 
                end_date= datetime.combine(data_fixa.date(), time.max))
    }
    return data
