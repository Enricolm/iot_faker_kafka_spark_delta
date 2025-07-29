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
- **Docker Compose** – Orquestração dos containers (Kafka, Zookeeper, Spark, etc.).
- **Python (Faker)** – Geração de dados IoT simulados.

## **⚡ Execução do Projeto**

Executar o processo por completo:
    
    ```PowerShell
    docker compose up -d
    ```

## **Validar resultados**

    ```PowerShell
    docker exec -it pyspark-consumer spark-submit --packages io.delta:delta-core_2.12:2.4.0 /app/spark/consultando_dados.py
    ```
