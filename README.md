## PROJETO 1

# 🧭 Diário de Bordo - Pipeline de Dados com PySpark e Delta Lake

Este projeto implementa um pipeline de processamento de dados utilizando **Apache Spark**, com foco em dados de deslocamento (categoria, distância, propósito, etc.), permitindo o agrupamento, validação e tratamento de dados inválidos em uma arquitetura moderna com **Delta Lake**.

## 🔄 Fluxo de Processamento

1. **Leitura da Camada Bronze**
   - Os dados brutos são carregados a partir de arquivos CSV com formatação de datas personalizada.

2. **Validação dos Dados**
   - As linhas com colunas nulas (ex: `CATEGORIA`, `PROPOSITO`, `DISTANCIA`, `DATA_INICIO`) são filtradas.
   - Dados inválidos são armazenados em uma **tabela de quarentena** para análise posterior.

3. **Transformações**
   - As datas são convertidas para o padrão `yyyy-MM-dd`.
   - Agregações como média, máximo, mínimo e contagens por categoria e propósito são aplicadas.

4. **Gravação na Camada Silver**
   - Os dados transformados e agregados são salvos em formato Delta, particionados por data (`dt_refe`).

## 📁 Estrutura de Pastas

``` bash
diario_de_bordo/
├── app/
│ ├── DiarioDeBordo/
│ │ ├── DiarioDeBordoExecute.py
│ │ ├── DiarioDeBordoTransform.py
│ │ ├── DiarioDeBordoEnum.py
│ │ ├── DiarioDeBordoCreateTable.py
│ │ └── LoggerService.py
├── data/
│ └── bronze/
└── README.md
```

## 🛠️ Tecnologias Utilizadas

- Apache Spark
- Delta Lake
- PySpark
- Databricks
- Python 3.10

## 🚨 Tratamento de Erros

- Logs são gerenciados com o módulo `logging`, com exibição no console.
- Estrutura pronta para integração com tabelas de erro se necessário.

## 📌 Objetivo

Garantir o controle e a rastreabilidade de dados de transporte, permitindo análises confiáveis mesmo em ambientes com dados incompletos ou inconsistentes.

Notebook: https://dbc-35f07cc0-9f86.cloud.databricks.com/login.html?next_url=%2Feditor%2Fnotebooks%2F3406324339502378%3Fo%3D2187747513666326&tuuid=89c103bb-0583-466f-9b17-9f0d8efcd0a2#command/6501943768248975

github: https://github.com/Enricolm/diario_de_bordo/tree/main


## PROJETO 2
## **📜 Descrição do Projeto**

Este projeto demonstra uma arquitetura de **streaming de dados em tempo real** utilizando **Kafka**, **PySpark (Structured Streaming)** e **Delta Lake**.  
Ele simula dispositivos IoT que enviam dados para um tópico Kafka, que são consumidos e processados em tempo real pelo PySpark e armazenados no formato Delta Lake.


## **🔎 Fluxo de Dados**

1. **IoT Simulator**  
   - Gera dados fake usando a biblioteca **Faker**.  
   - Cria uma Api que simula o funcionamento de um iot.

2. **Kafka**  
   - Atua como um **message broker**, recebendo os dados do simulador e garantindo a entrega para o consumidor.  
   - Mantém os dados particionados e replicados para garantir tolerância a falhas.

3. **PySpark Structured Streaming**  
   - Consome dados diretamente do tópico Kafka.  
   - Faz o parsing do JSON recebido.  
   - Enriquecimento e padronização dos dados (ex.: truncar a data para granularidade horária).  
   - Persiste os dados no **Delta Lake** (camada *bronze*).


4. **Delta Lake**  
   - Tabela transacional armazenada em `/data/delta/bronze/iot_emulado`.  
   - Suporte a versionamento, esquema evolutivo e alta confiabilidade.


## **🛠️ Tecnologias Utilizadas**

- **Apache Kafka** – Mensageria e ingestão de dados em tempo real.
- **Apache Spark (PySpark)** – Processamento distribuído em streaming.
- **Delta Lake** – Armazenamento confiável com suporte ACID.
- **Docker Compose** – Orquestração dos containers (Kafka, Zookeeper, Spark).
- **Python (Faker)** – Geração de dados IoT simulados.

## Estrutura de pasta

```bash
IOT_FAKER_KAFKA_SPARK_DELTA/
├── app/
│   ├── kafka/                   
│   │   ├── error/
│   │   └── producer.py
│   ├── service/                  
│   │   ├── __pycache__/
│   │   ├── Exception.py
│   │   └── LoggerService.py
│   ├── spark/                    
│   │   ├── error/
│   │   ├── consultando_dados.py
│   │   ├── consumer.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
├── delta/
│   └── bronze/
│       └── iot_emulado/         
├── iot_simulator/               
│   ├── __pycache__/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── .gitignore
├── docker-compose.yml
└── README.md
```


## **⚡ Execução do Projeto**

Executar o processo por completo:
    
    
    docker compose up --build -d
    

## **👤 Autor**

**Enrico Lopes Malachini**  
📧 **E-mail:** [rico.malachini@gmail.com](mailto:rico.malachini@gmail.com)  
🔗 **GitHub:** [github.com/Enricolm](https://github.com/Enricolm)  
🔗 **LinkedIn:** [linkedin.com/in/enrico-malachini](https://www.linkedin.com/in/enrico-malachini)

