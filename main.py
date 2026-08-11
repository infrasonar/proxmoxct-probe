from libprobe.probe import Probe
from lib.check.ct import CheckCT
from lib.check.firewall import CheckFirewall
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckCT,
        CheckFirewall,
    )

    probe = Probe("proxmoxct", version, checks)

    probe.start()
