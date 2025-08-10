
import time
from random import uniform
import paho.mqtt.client as mqtt
from confluent_kafka import Producer

# ---------- Konfiguration ----------------------------------------------------
MQTT_BROKER   = "mqtt.eclipseprojects.io"
MQTT_TOPIC    = "temperature3"

KAFKA_BOOTSTRAP = "localhost:9092"
KAFKA_TOPIC     = "temperature3"
# -----------------------------------------------------------------------------

# MQTT-Producer ---------------------------------------------------------------
mqtt_client = mqtt.Client(client_id="mqtt_bridge_producer")
mqtt_client.connect(MQTT_BROKER)

# Kafka-Producer --------------------------------------------------------------
kafka_conf = {
    "bootstrap.servers": KAFKA_BOOTSTRAP,
    "client.id": "mqtt_bridge_producer",
    "acks": "all",
}
kafka_producer = Producer(kafka_conf)

def delivery_report(err, msg):
    if err:
        print(f"[Kafka] Delivery failed: {err}")
    else:
        print(f"[Kafka] Message delivered to {msg.topic()} [{msg.partition()}] "
              f"offset {msg.offset()}")

# Loop ------------------------------------------------------------------------
try:
    while True:
        value = round(uniform(20.0, 21.0), 2)

        # MQTT
        mqtt_client.publish(MQTT_TOPIC, payload=value, qos=0, retain=False)
        print(f"[MQTT ] published {value} to {MQTT_TOPIC}")

        # Kafka
        kafka_producer.produce(
            topic=KAFKA_TOPIC,
            value=str(value).encode("ascii"),
            on_delivery=delivery_report
        )
        kafka_producer.poll(0)      # trigger delivery callbacks

        time.sleep(3)

except KeyboardInterrupt:
    print("Interrupted – exiting …")
finally:
    kafka_producer.flush(5)
    mqtt_client.disconnect()
