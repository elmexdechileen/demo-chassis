from json import dumps
from kafka import KafkaProducer
from ksql import KSQLAPI

class MockSink():

  def connect(self):
    raise NotImplementedError()

  def send(self, message):
    raise NotImplementedError()


class KafkaSink(MockSink):
  def __init__(self, broker, topic):
    print(f"Connecting to sink at {broker}")

    self._topic = topic

    self._producer = KafkaProducer(bootstrap_servers=[broker],
                            value_serializer=lambda x:
                            dumps(x).encode('utf-8'))

  def connect(self, ):
    return True

  def send(self, message):
    # Send Mock object
    self._producer.send(self._topic, value=message)

class OracleSink(MockSink):
  def __init__(self, hostname, port, service):
    print(f"Connecting to sink at {hostname}")

    self._dsn_tns = cx_Oracle.makedsn(hostname, port, service_name=service)

    self._producer = KafkaProducer(bootstrap_servers=[broker],
                            value_serializer=lambda x:
                            dumps(x).encode('utf-8'))

  def connect(self, user, password):
    self._conn = cx_Oracle.connect(user=user, password=password, dsn=self._dsn_tns) 
    return True

  def send(self, message):
    # Send Mock object
    c = conn.cursor()
    c.execute(query) # use triple quotes if you want to spread your query across multiple lines
    for row in c:
        print (row[0], '-', row[1]) # this only shows the first two columns. To add an additional column you'll need to add , '-', row[2], etc.
    conn.close()

