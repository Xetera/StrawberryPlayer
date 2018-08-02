from .packet import Packet


class WebsocketRequestException(Packet):
    def __init__(self, **kwargs):
        super(
            header=kwargs.get('header', 'error'),
            body=kwargs.get('body', 'Unexpected server error'),
            user='StrawberryServer'
        )
