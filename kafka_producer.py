from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
for i in range(10):
    future =producer.send('my_topic',b'some_message_%d' % i)
    result = future.get(timeout=60)