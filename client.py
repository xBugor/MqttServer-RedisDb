import paho.mqtt.client as mqtt
import time

broker = '37b23d1e7dfa49e5837444cc03ada058.s1.eu.hivemq.cloud'
port = 8883
topic = "test"
message = "Onur"

print('MQTT Client Başlatılıyor...')


client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print(f"Bağlantı başarılı, kod: {rc}")
    if rc == 0:  
        print("Bağlantı başarılı!")
        client.subscribe(topic)  
        client.publish(topic, message, qos=1)  
        print(f"Mesaj gönderildi: {message}")
    else:
        print(f"Bağlantı hatası: {rc}")

client.on_connect = on_connect

client.connect(broker, port)

client.loop_start()

time.sleep(5)

client.loop_stop()

print("Bağlantı ve mesaj gönderme işlemi tamamlandı.")
