# 🏍️ Mottu Smart Monitor — Sprint 4  
### Disruptive Architectures: IoT, IoB & Generative IA

---

## 📘 Descrição do Projeto  
O **Mottu Smart Monitor** é uma solução desenvolvida para **gerenciar e reduzir perdas de lucro da Mottu**, utilizando conceitos de **Internet das Coisas (IoT)** e **arquiteturas disruptivas**.  

O sistema foi projetado para simular o comportamento de dispositivos IoT instalados nas motos da empresa, coletando dados em tempo real (status, temperatura, bateria, etc.) e enviando-os para um **servidor Flask**.  
Esses dados são exibidos em um **dashboard web** desenvolvido com **HTML, CSS e JavaScript**, que mostra as informações atualizadas automaticamente via **WebSocket**.

---

## 🧠 Objetivo  
O objetivo do projeto é demonstrar o uso de **tecnologias emergentes** aplicadas à gestão operacional, criando um fluxo de dados completo entre dispositivos simulados e um ambiente de visualização interativo.  

Isso permite que gestores monitorem a frota e **identifiquem rapidamente fatores que contribuem para perdas financeiras**, como veículos parados, excesso de manutenção ou falhas operacionais.

---

## ⚙️ Arquitetura da Solução  

```
Simulador IoT (Python)
    ↓ Envia dados JSON via HTTP
Servidor Flask (API REST + SocketIO)
    ↓
Dashboard Web (HTML, CSS e JavaScript)
```

---

## 💡 Tecnologias Utilizadas  

| Camada | Tecnologia | Função |
|--------|-------------|--------|
| IoT Simulation | Python | Geração e envio de dados simulados |
| Backend API | Flask + Flask-SocketIO + Flask-CORS | Recebimento e distribuição dos dados |
| Frontend Web | HTML, CSS, JavaScript | Visualização em tempo real |
| Comunicação | HTTP + WebSocket | Integração entre componentes |

---

## 🧩 Estrutura de Pastas  

```
📂 Sprint4-IoT/
 ├── static/
 │   └── dashboard.html        # Dashboard web (interface em tempo real)
 ├── server.py                 # API Flask + SocketIO
 ├── Simulador_IoT.py          # Simulador de dispositivos IoT
 └── README.md                 # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto  

### 1️⃣ Instalar Dependências  
No terminal, execute:
```bash
python -m pip install flask flask-cors flask-socketio requests
```

---

### 2️⃣ Iniciar o Servidor Flask  
```bash
python server.py
```
O servidor iniciará em:  
```
http://localhost:3000
```

---

### 3️⃣ Abrir o Dashboard  
Acesse no navegador:  
```
http://localhost:3000
```
A página exibirá uma tabela que será atualizada em tempo real conforme os dados chegarem.

---

### 4️⃣ Executar o Simulador IoT  
```bash
python Simulador_IoT.py
```
O script começará a gerar e enviar dados aleatórios simulando dispositivos conectados.  
O dashboard exibirá cada leitura em tempo real.

---

## 📈 Resultados Esperados  

- Monitoramento em tempo real da frota.  
- Detecção rápida de motos paradas ou em manutenção.  
- Visualização de métricas de temperatura e bateria.  
- Demonstração prática de **arquitetura IoT integrada com WebSocket**.  

---

## 🤖 Futuras Melhorias (IA Generativa)  
- Geração de relatórios automáticos com insights sobre desempenho.  
- Análise preditiva de falhas e perdas operacionais.  
- Uso de IA generativa para explicar causas de perda de lucro.  

---

## 👨‍💻 Equipe  

- **Kauã Fermino Zipf** – RM: 558957  
- **Caetano Matos Penafiel** – RM: 557984
- **Victor Egidio Lira** - RM: 556653
- **Turma:** 2TDSPG — Challenge 2025 — 2º Semestre  
- **Instituição:** FIAP — Faculdade de Informática e Administração Paulista  

---

## 🏁 Conclusão  

O **Mottu Smart Monitor** demonstra a aplicação de tecnologias disruptivas em um contexto real de negócio.  
Por meio da integração entre **IoT, APIs e visualização em tempo real**, o projeto apresenta uma arquitetura moderna, escalável e inovadora para análise de operações e redução de perdas financeiras.  
Esta entrega cumpre integralmente os requisitos da **Sprint 4 — Disruptive Architectures: IoT, IoB & Generative IA**.
