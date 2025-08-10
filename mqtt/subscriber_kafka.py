from confluent_kafka import Consumer, KafkaException, KafkaError

# ---------- Konfiguration ----------------------------------------------------
KAFKA_BOOTSTRAP = "50.85.98.227:9092"
KAFKA_TOPIC     = "temperature3"
GROUP_ID        = "temp_reader"
# -----------------------------------------------------------------------------

conf = {
    "bootstrap.servers": KAFKA_BOOTSTRAP,
    "group.id": GROUP_ID,
    "auto.offset.reset": "latest",     # ab neuen Nachrichten lesen
}

consumer = Consumer(conf)
consumer.subscribe([KAFKA_TOPIC])

print("-- waiting for messages --")
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue          # timeout
        if msg.error():
            if msg.error().code() != KafkaError._PARTITION_EOF:
                raise KafkaException(msg.error())
            continue
        value = msg.value().decode("ascii")
        print(f"[Kafka] received {value} from {msg.topic()} offset {msg.offset()}")

except KeyboardInterrupt:
    print("Interrupted – exiting …")
finally:
    consumer.close()
