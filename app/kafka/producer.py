import json
import time
import requests
from kafka import KafkaProducer
from service.LoggerService import LoggerService
from service.Exception import IotProducerException, ApiConnectionError, KafkaSendError

log = LoggerService('producer').get_logger()

producer = (
    KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer = lambda Value: json.dumps(Value).encode('utf-8')
    )
)
log.info('Producer Kafka instanciado com sucesso.')

indexador_error = 0

while True:

    if indexador_error == 5:
        break 
    
    responseIotEmulado = (
        requests.get(
            "http://iot-simulator:5000/iot-data"
        )
    )

    try:

        if responseIotEmulado.status_code != 200:
            raise ApiConnectionError(f'Erro para se conectar com a API do iot.')

        log.info(f'Status Code retornado pelo IOT EMULADO: {responseIotEmulado.status_code}')
        
        dataIotEmulado = responseIotEmulado.json()

        log.info(f"Dados recebidos: {dataIotEmulado}")

        try:
            producer.send('iot_topic', value=dataIotEmulado)
            log.info(f'Dados Enviados Para o Topico: iot_topic')

        except Exception as e:
            raise KafkaSendError(f'Erro para enviar os dados no topico do Kafka.')

        time.sleep(2)

    except ApiConnectionError as e:
        indexador_error += 1 
        log.error(f'{e} \n Data: {dataIotEmulado}')

    except KafkaSendError as e:
        indexador_error += 1 
        log.error(f'{e} \n Data: {dataIotEmulado}')
    
    except IotProducerException as e:
        indexador_error += 1
        log.error(f'{e}')
