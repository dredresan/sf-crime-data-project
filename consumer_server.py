from pykafka import KafkaClient
import logging

logging.getLogger("pykafka.broker").setLevel('ERROR')

client = KafkaClient(hosts="localhost:9092")
topic = client.topics["police-calls"]

consumer = topic.get_balanced_consumer(
    auto_commit_enable = False,
    zookeeper_connect = 'localhost:2181',
    consumer_group = 'police_calls_consumer_group'
)

# Print out the messages
# This is similar to when consuming messages on the command line:
# kafka-console-consumer --bootstrap-server localhost:9092 --topic police-calls --from-beginning
for message in consumer:
    if message is not None:
        print(message.value.decode('utf-8'))
