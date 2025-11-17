from libprobe.probe import Probe
from lib.check.ct import CheckCT
from lib.version import __version__ as version


if __name__ == '__main__':
    checks = (
        CheckCT,
    )

    probe = Probe("proxmoxct", version, checks)

    probe.start()
