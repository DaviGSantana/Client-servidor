# Client-servidor

Este projeto implementa um modelo de **cliente-servidor** utilizando **sockets TCP e UDP em Python**.  
O objetivo é demonstrar a comunicação em rede entre processos, permitindo o envio e recebimento de mensagens entre clientes e servidor, tanto no protocolo orientado a conexão (TCP) quanto no protocolo sem conexão (UDP).  

---

## 🚀 Funcionalidades

- 🌐 **Servidor**: Escuta conexões TCP e mensagens UDP, processando e respondendo a múltiplos clientes.
- 💻 **Cliente TCP**: Estabelece conexão com o servidor e troca mensagens via protocolo TCP.
- 📡 **Cliente UDP**: Envia e recebe mensagens do servidor via protocolo UDP.
- 🧾 **Exemplo didático**: Ideal para estudo de programação de redes e sockets.

---

## 📂 Estrutura do Projeto

- `servidor.py` → Implementação do servidor TCP/UDP.  
- `clientTCP.py` → Implementação do cliente TCP.  
- `clientUDP.py` → Implementação do cliente UDP.  

---

## 🛠️ Requisitos

- Python **3**  
- Bibliotecas padrão (`socket`, `sys`)  

---

## ▶️ Como Usar

### 1️⃣ Executar o Servidor
No terminal, execute o comando:

```bash
python servidor.py
