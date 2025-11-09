import requests
import random
import time
import json

# URL do backend ou dashboard que receberá os dados
# Pode ser local (ex: http://localhost:5000/data) ou em nuvem
URL = "http://localhost:3000/api/motos"  # altere para o endpoint real

# Lista simulada de IDs de motos
motos = ["MOTTU-001", "MOTTU-002", "MOTTU-003"]

# Status possíveis
status_op = ["em uso", "parada", "manutenção"]

def gerar_dados_moto(moto_id):
    """Gera dados aleatórios simulando um dispositivo IoT."""
    return {
        "moto_id": moto_id,
        "status": random.choice(status_op),
        "latitude": round(random.uniform(-23.6, -23.4), 6),
        "longitude": round(random.uniform(-46.7, -46.5), 6),
        "bateria": random.randint(20, 100),  # porcentagem
        "temperatura_motor": round(random.uniform(25, 80), 2),  # °C
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

def enviar_dados():
    """Envia dados aleatórios a cada intervalo de tempo."""
    print("🚀 Iniciando simulação de dispositivos IoT da Mottu...\n")
    while True:
        for moto in motos:
            dados = gerar_dados_moto(moto)
            try:
                response = requests.post(URL, json=dados)
                if response.status_code in [200, 201]:
                    print(f"✅ Dados enviados: {json.dumps(dados, indent=2)}")
                else:
                    print(f"⚠️ Erro ao enviar dados ({response.status_code}): {response.text}")
            except Exception as e:
                print(f"❌ Falha na conexão: {e}")

            # Espera alguns segundos antes de enviar o próximo pacote
            time.sleep(3)

if __name__ == "__main__":
    enviar_dados()
