from config import langnet_config
from langnet.bridge import bridge
import time

if __name__ == "__main__":
    bridge = bridge.Bridge(langnet_config)
    print(bridge.config.__dict__)
    i = 0
    while True:
        # WIP, testing, TBD
        print('langnet running', i)
        i += 2
        time.sleep(1)
        if i > 10:
            break
