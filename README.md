# 🏍️ Mottu Smart Monitor — Sprint 4  
### Disruptive Architectures: IoT, IoB & Generative IA

---

## 📘 Descrição do Projeto  
O **Mottu Smart Monitor** é uma solução desenvolvida para **gerenciar e reduzir perdas de lucro da Mottu**, utilizando conceitos de **Internet das Coisas (IoT)** e **arquiteturas disruptivas**.  

O sistema simula o comportamento de dispositivos IoT instalados nas motos da empresa, coletando dados em tempo real (status, temperatura, bateria, etc.) e enviando-os para um **servidor Flask**.  
Esses dados são exibidos em um **dashboard web** desenvolvido com **HTML, CSS e JavaScript**, que apresenta as informações atualizadas automaticamente via **WebSocket**.  

Além disso, o projeto inclui um **aplicativo mobile (Expo/React Native)** que exibe o dashboard em uma interface otimizada, com suporte a **modo escuro/claro** e um **botão de recarregamento**.

---

## 🧠 Objetivo  
Demonstrar o uso de **tecnologias emergentes** aplicadas à gestão operacional, criando um fluxo de dados completo entre dispositivos simulados, um servidor intermediário e interfaces web/mobile.  

Com isso, a solução permite que gestores monitorem a frota em tempo real e **identifiquem rapidamente fatores que contribuem para perdas financeiras**, como veículos parados, baixa bateria, temperatura elevada ou necessidade de manutenção.

---

## ⚙️ Arquitetura da Solução  

```
Simulador IoT (Python)
    ↓ Envia dados JSON via HTTP
Servidor Flask (API REST + SocketIO)
    ↓
Dashboard Web (HTML, CSS e JavaScript)
    ↓
App Mobile (React Native + WebView)
```

---

## 💡 Tecnologias Utilizadas  

| Camada | Tecnologia | Função |
|--------|-------------|--------|
| IoT Simulation | Python | Geração e envio de dados simulados (10 motos virtuais) |
| Backend API | Flask + Flask-SocketIO + Flask-CORS | Recebimento, broadcast e atualização em tempo real |
| Frontend Web | HTML5 + CSS3 + JavaScript | Dashboard dinâmico e responsivo |
| Mobile App | React Native + Expo + WebView | Exibição mobile do dashboard com recarregamento manual |
| Comunicação | HTTP + WebSocket | Envio contínuo e sincronização instantânea de dados |

---

## 🧩 Estrutura de Pastas  

```
📂 MottuSmartMonitor/
 ├── backend_iot/
 │   ├── server.py              # Servidor Flask + SocketIO
 │   ├── Simulador_IoT.py       # Simulador de 10 motos (dados IoT)
 │   └── static/
 │       └── dashboard.html     # Dashboard web responsivo
 │
 └── mobile_app/
     └── MottuMonitor/
         └── app/
             └── _layout.tsx    # App mobile com WebView e botão "Recarregar"
```

---

## 🚀 Como Executar o Projeto  

### 🧱 1️⃣ Instalar Dependências (Backend)
```bash
python -m pip install flask flask-cors flask-socketio requests
```

---

### 🔥 2️⃣ Iniciar o Servidor Flask
```bash
python server.py
```
O servidor iniciará em:  
```
http://localhost:3000
```

---

### ⚙️ 3️⃣ Executar o Simulador IoT
```bash
python Simulador_IoT.py
```
O simulador gera dados de 10 motos virtuais (status, bateria, temperatura, etc.) e envia ao servidor.  

Os dados são exibidos em tempo real no dashboard.

---

### 💻 4️⃣ Acessar o Dashboard
Abra no navegador:
```
http://localhost:3000
```

O dashboard mostrará as leituras em tempo real, com **layout adaptável**, **modo escuro/claro automático** e **atualização instantânea via WebSocket**.

---

### 📱 5️⃣ Executar o App Mobile (Expo)
1. Entre na pasta do projeto mobile:
   ```bash
   cd mobile_app/MottuMonitor
   ```
2. Instale a dependência:
   ```bash
   npx expo install react-native-webview
   ```
3. Rode o app:
   ```bash
   npx expo start
   ```
4. No celular (com **Expo Go** instalado), escaneie o QR Code.

> 💡 **Importante:**  
> Edite o arquivo `_layout.tsx` e altere o valor da constante `dashboardUrl` para o **IP do seu computador**, por exemplo:
> ```tsx
> const dashboardUrl = "http://192.168.0.10:3000";
> ```

---

## 🌈 Funcionalidades do Dashboard  

- **Responsivo:** layout se adapta automaticamente a telas pequenas (celulares e tablets).  
- **Modo Escuro/Claro Automático:** ajusta cores de acordo com o tema do sistema.  
- **Atualização Instantânea:** novos dados aparecem assim que o simulador envia.  
- **Visualização Completa:** status da moto, bateria, temperatura, localização e horário.  

---

## 📲 Funcionalidades do App Mobile  

- Exibe o **mesmo dashboard** hospedado no servidor Flask.  
- Botão **"⟳ Recarregar"** para atualizar manualmente o WebView.  
- Design consistente com o tema escuro e o estilo do dashboard.  
- Integração direta via rede local (HTTP).  

---

## 📈 Resultados Esperados  

- Monitoramento em tempo real da frota de motos da Mottu.  
- Identificação rápida de falhas e anomalias.  
- Detecção de padrões de manutenção e uso.  
- Redução de perdas financeiras com **decisões baseadas em dados**.  
- Demonstração prática de **arquitetura IoT integrada com Mobile e WebSocket**.  

---

## 🤖 Futuras Melhorias (IA Generativa)  

- **Análise preditiva de falhas:** prever quando uma moto precisará de manutenção.  
- **Insights automáticos:** IA gera relatórios sobre desempenho e custos.  
- **Assistente inteligente:** integração com modelo generativo para explicar causas de perdas.  

---

## 👨‍💻 Equipe  

- **Kauã Fermino Zipf** – RM: 558957  
- **Caetano Matos Penafiel** – RM: 557984  
- **Victor Egidio Lira** – RM: 556653  
- **Turma:** 2TDSPG — Challenge 2025 — 2º Semestre  
- **Instituição:** FIAP — Faculdade de Informática e Administração Paulista  

---

## 🏁 Conclusão  

O **Mottu Smart Monitor** representa a convergência entre **IoT, APIs, Web e Mobile**, resultando em uma solução inovadora, escalável e funcional.  

Por meio da integração entre o **simulador de dispositivos inteligentes**, o **servidor Flask** e o **dashboard em tempo real**, o sistema fornece uma visão operacional precisa, auxiliando na **tomada de decisões estratégicas** e na **redução de perdas de lucro**.  

O projeto atende integralmente os objetivos da **Sprint 4 — Disruptive Architectures: IoT, IoB & Generative IA**, demonstrando aplicação prática de tecnologias emergentes e experiência real de integração multidisciplinar.
