from kafka import kafkaConsumer, kafkaProducer

consumer = kafkaConsumer('my_topic',group_id='my_group')
consumer.assign([TopicPartition('my_topic', 2)])
msg = next(consumer)
print(f"Received message: {msg.value}")
for msg in consumer:
    print(f"Received message: {msg.value}")