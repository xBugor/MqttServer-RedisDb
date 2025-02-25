import paho.mqtt.client as mqtt
import ssl
import certifi

# Callback fonksiyonları
def on_connect(client, userdata, flags, rc):
    print(f"Bağlantı durumu: {rc}")
    if rc == 0:
        print("Bağlantı başarılı!")
        client.subscribe("test")  # "test" topic'ine abone ol
    else:
        print(f"Bağlantı başarısız, hata kodu: {rc}")

def on_message(client, userdata, msg):
    print(f"Mesaj alındı: {msg.topic} -> {msg.payload.decode()}")  # Mesajı yazdır

# Broker URL ve portu
broker_url = "37b23d1e7dfa49e5837444cc03ada058.s1.eu.hivemq.cloud"  # HiveMQ Cloud broker URL'si
broker_port = 8883  # SSL portu (güvenli bağlantı için)

# MQTT istemcis
# i oluştur
client = mqtt.Client()

# Kullanıcı adı ve şifre ayarla
client.username_pw_set("onur61", "Onur6125")  # HiveMQ Cloud kimlik bilgileri

# Callback fonksiyonlarını tanımla
client.on_connect = on_connect
client.on_message = on_message

# 🔹 Sertifika doğrulama ayarları (GÜNCEL VE DOĞRU)
client.tls_set(certifi.where(), tls_version=ssl.PROTOCOL_TLS_CLIENT)  

# Broker'a bağlan
client.connect(broker_url, broker_port, 60)

# Mesajları almak için sürekli dinleme başlat
client.loop_forever()
