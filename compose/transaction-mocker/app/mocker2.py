"""Load configuration from .yaml file."""
import confuse
from faker import Faker
from time import sleep

from sink import KafkaSink

fake = Faker()
config = confuse.Configuration('mocker')
config.set_file('config.yaml')

rate = config['transactions']['rate'].get(int)

# Define mock format


# Connect to mock sink
sink = KafkaSink(
  broker=config['kafka']['broker'].get(),
  topic=config['kafka']['topic'].get()
)
sink.connect()


print("Start sending transactions")
while True:
    # Create mock object
    message = {
      'transaction_id': "RT" + str(fake.pyint(5)),
      'from_account': fake.iban(),
      'to_account': fake.iban(),
      'amount_cents': fake.pyint(),
      'created_at': fake.date_time().strftime("%Y/%m/%d, %H:%M:%S")
    }

    sink.send(message)

    sleep(rate)


