import time
from sc3f import Server_MGMT, Synths_MGMT

is_server_up = False
servers = Server_MGMT()
synth_setup = Synths_MGMT()

while True:
    try:
        if not is_server_up:
            s = servers.server_boot()
            is_server_up = True
            synth_setup.set_synth()
        time.sleep(20)
    except KeyboardInterrupt:
        if is_server_up:
            servers.server_quit(s)
        break