import paho.mqtt.client as mqtt

# MQTT broker bilgileri
broker = '10.141.0.86'
port = 1883
topic = "test"
message = "Emrullah"
# Mesaj alındığında çağrılan fonksiyon
def on_message(client, userdata, msg):
    print(f"Gelen Mesaj: {msg.topic}: {msg.payload.decode()}")

# MQTT istemcisi oluştur
client = mqtt.Client()

# Olay fonksiyonlarını tanımla
client.on_message = on_message

# Broker'a bağlan
client.connect(broker, port, 60)

# Belirli bir konuyu dinle
client.subscribe(topic)

# Mesajları sürekli dinle
client.loop_forever()
