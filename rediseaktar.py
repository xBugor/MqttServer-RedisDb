import paho.mqtt.client as mqtt
import redis
import time

broker = 'd90fa1f655de46ab96e6ba4976d0c6c8.s1.eu.hivemq.cloud'
port = 8883
topic = "test"

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def on_message(client, userdata, msg):
    print(f"Bağlantı başarılı")
    mesaj = msg.payload.decode()
    print(f"Gelen Mesaj: {mesaj}")

    redis_client.rpush(topic, mesaj) 

mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

mqtt_client.connect(broker, port, 60)

mqtt_client.subscribe(topic, qos=1)  

mqtt_client.loop_start()  

while True:
    time.sleep(1) 
