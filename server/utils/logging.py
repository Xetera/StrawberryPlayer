import logging
import os


def create_logger():
    format = '%(asctime)-s [%(levelname)s]: %(message)s'

    fh = logging.FileHandler('server.log')
    fh.setLevel('DEBUG')

    ch = logging.StreamHandler()
    ch.setLevel('ERROR')
    formatter = logging.Formatter(format)
    logging.basicConfig(
        format=format,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    out = logging.getLogger('StrawberryServer')

    log_level = os.environ.get('STRAWBERRY_LOG_LEVEL', 'INFO')
    if log_level not in ['DEBUG', 'INFO', 'WARNING', 'ERROR']:
        log_level = 'INFO'

    out.setLevel(log_level)
    out.addHandler(fh)
    out.addHandler(ch)
    return out


logger = create_logger()
