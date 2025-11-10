import requests
import random
import time
import json
from datetime import datetime

URL = "http://localhost:3000/api/motos"

motos = [
    "MOTTU-001", "MOTTU-002", "MOTTU-003", "MOTTU-004", "MOTTU-005",
    "MOTTU-006", "MOTTU-007", "MOTTU-008", "MOTTU-009", "MOTTU-010"
]

status_op = ["em uso", "parada", "manutenção"]

def gerar_dados_moto(moto_id):
    """Gera dados aleatórios simulando sensores IoT de uma moto."""
    return {
        "moto_id": moto_id,
        "status": random.choice(status_op),
        "latitude": round(random.uniform(-23.7, -23.4), 6),
        "longitude": round(random.uniform(-46.8, -46.4), 6),
        "bateria": random.randint(10, 100),
        "temperatura_motor": round(random.uniform(25, 90), 2)
    }

def enviar_dados():
    """Gera e envia dados continuamente para o servidor Flask."""
    print("🚀 Iniciando simulação de dispositivos IoT da Mottu...\n")
    while True:
        for moto in motos:
            dados = gerar_dados_moto(moto)
            try:
                response = requests.post(URL, json=dados)
                if response.status_code in [200, 201]:
                    print(f"✅ Enviado para dashboard: {json.dumps(dados, indent=2, ensure_ascii=False)}\n")
                else:
                    print(f"⚠️ Erro ({response.status_code}): {response.text}")
            except Exception as e:
                print(f"❌ Falha na conexão: {e}")
            time.sleep(1)  
        print("-----------------------------------------------------------")
        print(f"📡 Ciclo completo enviado às {datetime.now().strftime('%H:%M:%S')}")
        print("-----------------------------------------------------------\n")
        time.sleep(3)  

if __name__ == "__main__":
    enviar_dados()
