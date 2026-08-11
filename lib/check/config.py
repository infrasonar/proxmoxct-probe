from libprobe.asset import Asset
from libprobe.check import Check
from ..helpers import api_request
from ..utils import to_bool


class CheckConfig(Check):
    key = 'config'
    unchanged_eol = 14400

    @staticmethod
    async def run(asset: Asset, local_config: dict, config: dict) -> dict:
        uri = '/config'
        data = await api_request(asset, local_config, config, uri, 'lxc')
        config = data['data']
        config_item = {
            'name': 'config',  # str
            'arch': config.get('arch'),  # str
            'cores': config.get('cores'),  # int
            'description': config.get('description'),  # str
            'digest': config.get('digest'),  # str
            'features': config.get('features'),  # str
            'hostname': config.get('hostname'),  # str
            'memory': config.get('memory'),  # int
            'net0': config.get('net0'),  # str
            'net1': config.get('net1'),  # str
            'onboot': to_bool(config.get('onboot')),  # bool
            'ostype': config.get('ostype'),  # str
            'protection': to_bool(config.get('protection')),  # bool
            'rootfs': config.get('rootfs'),  # str
            'swap': config.get('swap'),  # int
            'tags': config.get('tags'),  # str
            'unprivileged': to_bool(config.get('unprivileged')),  # bool
        }

        state = {
            'config': [config_item],
        }

        return state
