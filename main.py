from libprobe.probe import Probe
from lib.check.ct import check_ct
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = {
        'ct': check_ct
    }

    probe = Probe("proxmoxct", version, checks)

    probe.start()
