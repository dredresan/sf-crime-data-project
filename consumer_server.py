from pykafka import KafkaClient
import logging

logging.getLogger("pykafka.broker").setLevel('ERROR')

client = KafkaClient(hosts="localhost:9092")
topic = client.topics["police-calls"]

consumer = topic.get_balanced_consumer(
    auto_commit_enable = False,
    zookeeper_connect = 'localhost:2181'
)

#Print out the messages
for message in consumer:
    if message is not None:
        print(message.value.decode('utf-8'))