from .packet import Packet


class WebsocketRequestException(Packet):
    def __init__(self, **kwargs):
        super(
        ).__init__(
            event=kwargs.get('event', 'error'),
            body=kwargs.get('body', 'Unexpected server error'),
            user='StrawberryServer'
        )
