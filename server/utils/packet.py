import json
from .logging import logger

def stringify(obj: dict) -> str:
    out = json.dumps(obj)
    logger.info(f'Stringified an object to size {len(out)}')
    return out