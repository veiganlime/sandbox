#!/usr/bin/env python3
import paho.mqtt.client as mqtt

BROKER = "4.175.150.20"        
PORT   = 1883
TOPIC  = "ba-demo/#"            

# MQTT v5-Callback-Signatur
def on_connect(client, userdata, flags, reasonCode, properties):
    if reasonCode == mqtt.CONNACK_ACCEPTED:
        print("✔ Verbunden zum Broker")
        # Ein Abo reicht – empfängt ba-demo/ba-demo-1 … ba-demo/ba-demo-4 usw.
        client.subscribe(TOPIC)          # QoS 0 (Standard)
    else:
        print(f"✖ Verbindungsfehler, reasonCode={reasonCode}")

def on_message(client, userdata, msg):
    # Nutzlast als UTF-8 ausgeben; Topic immer mit anzeigen
    print(f"📥 {msg.topic}: {msg.payload.decode(errors='replace')}")

client = mqtt.Client(client_id="subscriber", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
