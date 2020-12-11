"""Load configuration from .yaml file."""
import confuse
from faker import Faker
from time import sleep
from json import dumps
from kafka import KafkaProducer
from ksql import KSQLAPI
client = KSQLAPI('http://ksqldb-server:8088')

producer = KafkaProducer(bootstrap_servers=['broker:29092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

fake = Faker()
config = confuse.Configuration('mocker')
config.set_file('/app/config.yaml')

rate = config['transactions']['rate'].get(int)
topic = config['transactions']['topic'].get()

print("Start sending transactions")
while True:
    producer.send(topic, value={
      'transaction_id': "RF12111",
      'from_account': fake.iban(),
      'to_account': fake.iban(),
      'amount_cents': fake.pyint(),
      'created_at': fake.date_time().strftime("%Y/%m/%d, %H:%M:%S")
    })
    sleep(1/rate)
