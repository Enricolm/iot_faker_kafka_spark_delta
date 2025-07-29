class IotProducerException(Exception):
    """Exceção base para erros do IoT Producer."""
    pass


class ApiConnectionError(IotProducerException):
    """Erro ao conectar com a API do simulador IoT."""
    pass


class KafkaSendError(IotProducerException):
    """Erro ao enviar dados para o Kafka."""
    pass

class ConsumerException(Exception):
    """Erro customizado para o consumidor Spark."""
    pass