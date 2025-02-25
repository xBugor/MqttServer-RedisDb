import paho.mqtt.client as mqtt
import ssl
import certifi

# HiveMQ Cloud bağlantı bilgileri
BROKER = "37b23d1e7dfa49e5837444cc03ada058.s1.eu.hivemq.cloud"  # HiveMQ Cloud broker adresiniz
PORT = 8883  # TLS portu
USERNAME = "bugra"  # HiveMQ Cloud kullanıcı adı
PASSWORD = "Bugra123."  # HiveMQ Cloud şifresi
TOPIC = "test/topic"

# Bağlantı callback fonksiyonları
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Bağlantı başarılı!")
        client.subscribe(TOPIC)
        client.publish("test", "Onur Selamlar")
    else:
        print(f"Bağlantı hatası, kod: {rc}")

def on_message(client, userdata, msg):
    print(f"Gelen mesaj: {msg.payload.decode()}")

# MQTT istemcisi oluştur
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect
client.on_message = on_message

# Doğru TLS sertifikasını ayarla (ÖNCE tanımlanmalı!)
client.tls_set(certifi.where())

# HiveMQ Cloud'a bağlan
client.connect(BROKER, PORT, 60)

# Sürekli dinle
client.loop_forever()  