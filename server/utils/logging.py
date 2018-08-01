import logging
import os


def create_logger():
    format = '%(asctime)-15s [%(levelname)s]: %(message)s'

    fh = logging.FileHandler('server.log')
    fh.setLevel('DEBUG')

    ch = logging.StreamHandler()
    ch.setLevel('ERROR')
    formatter = logging.Formatter(format)
    logging.basicConfig(format=format)
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    out = logging.getLogger('StrawberryServer')

    log_level = os.environ.get('STRAWBERRY_LOG_LEVEL', 'INFO')
    if log_level not in ['DEBUG', 'INFO', 'WARNING', ]:
        raise EnvironmentError("STRAWBERRY_LOG_LEVEL environment set but is not valid")

    out.setLevel(log_level)
    out.addHandler(fh)
    out.addHandler(ch)
    return out


logger = create_logger()
