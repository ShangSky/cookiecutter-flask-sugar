from typing import Any, Dict

import yaml


def init_config(stream) -> Dict[str, Any]:
    return yaml.load(stream, Loader=yaml.FullLoader)
