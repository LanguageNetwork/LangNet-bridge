from langnet.bridge.config import BridgeConfig

langnet_config = BridgeConfig()

# dummy data for test
langnet_config.ROOT_CHAIN_CONTRACT_ADDRESS = "0xd5af31f24b80cd7f4c0049e06422836d6915b6a9"
langnet_config.ROOT_CHAIN_PROVIDER = "https://ropsten.infura.io"
langnet_config.ROOT_CHAIN_CONTRACT_ABI = "abi/rootchain.json"
langnet_config.SIDE_CHAIN_CONTRACT_ADDRESS = "0xd5af31f24b80cd7f4c0049e06422836d6915b6a9"
langnet_config.SIDE_CHAIN_CONTRACT_ABI = "abi/sidechain.json"
