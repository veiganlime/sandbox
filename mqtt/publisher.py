import json
import time
import paho.mqtt.client as mqtt

BROKER = "4.175.150.20"
PORT   = 1883

# ---------------------------------------------------------------------------
# 1) Pyload von Geräten
# ---------------------------------------------------------------------------
DEVICES = [
    {
        "client_id": "ba-demo-1",
        "topic":    "ba-demo/ba-demo-1",
        "payload":  {"strom": 10, "spannung": 230, "druck": 5, "volumenstrom": 50},
    },
    {
        "client_id": "ba-demo-2",
        "topic":    "ba-demo/ba-demo-2",
        "payload":  {"strom":  8, "spannung": 225, "druck": 6, "volumenstrom": 40},
    },
    {
        "client_id": "ba-demo-3",
        "topic":    "ba-demo/ba-demo-3",
        "payload":  {"strom": 12, "spannung": 235, "druck": 4, "volumenstrom": 60},
    },
    {
        "client_id": "ba-demo-4",
        "topic":    "ba-demo/ba-demo-4",
        "payload":  {"strom":  9, "spannung": 228, "druck": 7, "volumenstrom": 45},
    },
]

SEND_INTERVAL = 20          

# ---------------------------------------------------------------------------
# 2) Pro Gerät einen MQTT-Client anlegen
# ---------------------------------------------------------------------------
for dev in DEVICES:
    dev["client"] = mqtt.Client(client_id=dev["client_id"], protocol=mqtt.MQTTv5)
    dev["client"].connect(BROKER, PORT)
    dev["client"].loop_start()
    dev["seq"] = 0           

print("Läuft … (Strg-C beendet)")

# ---------------------------------------------------------------------------
# 3) Nachrichten in einer while - Schleife senden
# ---------------------------------------------------------------------------
try:
    while True:
        cycle_start = time.time()

        for dev in DEVICES:
            msg = {
                **dev["payload"],
                "device_id": dev["client_id"],
                "seq":       dev["seq"],
                "timestamp": int(time.time()*1000)  
            }
            result = dev["client"].publish(dev["topic"], json.dumps(msg))
            status = "✔" if result.rc == mqtt.MQTT_ERR_SUCCESS else "✖"
            print(f"{status} {dev['client_id']} → {dev['topic']}: {msg}")
            dev["seq"] += 1

        
        time.sleep(max(0, SEND_INTERVAL - (time.time() - cycle_start)))

except KeyboardInterrupt:
    print("\nBeende …")
finally:
    for dev in DEVICES:
        dev["client"].loop_stop()
        dev["client"].disconnect()
