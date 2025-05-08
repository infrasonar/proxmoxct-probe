from typing import Optional, Any
from libprobe.asset import Asset
from ..helpers import api_request


def to_float(inp: Any) -> Optional[float]:
    return inp if inp is None else float(inp)


async def check_ct(
        asset: Asset,
        asset_config: dict,
        config: dict) -> dict:
    uri = '/status/current'
    data = await api_request(asset, asset_config, config, uri, 'lxc')
    ct = data['data']
    ha = ct.get('ha')
    item = {
        'name': ct.get('name'),
        'vmid': ct['vmid'],  # int
        'cpu': to_float(ct.get('cpu')),  # float
        'cpus': ct.get('cpus'),  # int
        'disk': ct.get('disk'),  # int
        'swap': ct.get('swap'),  # int
        'maxswap': ct.get('maxswap'),  # int
        'diskread': ct.get('diskread'),  # int
        'diskwrite': ct.get('diskwrite'),  # int
        'maxdisk': ct.get('maxdisk'),  # int
        'maxmem': ct.get('maxmem'),  # int
        'mem': ct.get('mem'),  # int
        'netin': ct.get('netin'),  # int
        'netout': ct.get('netout'),  # int
        'pid': ct.get('pid'),  # int
        'status': ct['status'],  # str
        'uptime': ct.get('uptime'),  # int
    }
    state = {
        'ct': [item],
    }
    if ha is not None:
        state['ha'] = [{
            'name': 'ha',
            'managed': bool(ha.get('managed')),  # bool
        }]

    return state
