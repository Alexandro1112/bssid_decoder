import objc
import subprocess
import re
from CoreWLAN import CWNetwork, CWWiFiClient
import platform

if 'macOS' in platform.platform():
    objc.loadBundle(
        u"CoreWLAN",
        bundle_path=u"/System/Library/Frameworks/CoreWLAN.framework",
        module_globals=globals()
    )


    def get_bssid() -> str:
        """GET BSSID"""
        client = CWWiFiClient.sharedWiFiClient()
        iface = client.interfaceWithName_("en0")
        networks, error = iface.scanForNetworksWithName_error_(
            None,
            None,
        )
        return networks


    for i in get_bssid():
        bssid = re.sub('^bssid=', '', str(i).split('>')[1].split(', ')[1])
        for b in bssid.split():
            for j in range(len(bssid.split())):

                print(subprocess.getoutput(cmd=f"python decoder.py {b} --map",
                                           encoding="utf-8", errors=None))

else:
    quit('Error OS')
