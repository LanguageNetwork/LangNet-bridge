# from langnet.config import bridge_config
from web3 import Web3, HTTPProvider
from langnet.bridge.config import BridgeConfig
import json
import asyncio
from threading import Thread

class Bridge:
    config = BridgeConfig
    rootchain_web3 = None
    sidechain_web3 = None
    rootchain_contract = None
    sidechain_contract = None
    def __init__(self, BridgeConfig):
        self.config = BridgeConfig
        self.init_rootchain()
        print(self.rootchain_contract)

    def init_chain(self, provider):
        return Web3(HTTPProvider(provider))

    def init_rootchain(self):
        self.rootchain_web3 = self.init_chain(self.config.ROOT_CHAIN_PROVIDER)
        self.config.ROOT_CHAIN_CONTRACT_ADDRESS = self.rootchain_web3.toChecksumAddress(self.config.ROOT_CHAIN_CONTRACT_ADDRESS)
        rootchain_contract_abi = json.load(open(self.config.ROOT_CHAIN_CONTRACT_ABI, 'r'))
        self.rootchain_contract = self.rootchain_web3.eth.contract(
            address=self.rootchain_contract,
            abi=rootchain_contract_abi,
        )

    def handle_event(self, event):
        print(event)

    async def loop(self, event_filter, poll_interval):
        while True:
            for event in event_filter.get_new_entries():
                self.handle_event(event)
            await asyncio.sleep(poll_interval)

    def run(self):

        self.loop()
