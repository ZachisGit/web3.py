from web3.providers.rpc import TestRPCProvider


def test_miner_hashrate(web3_ipc_empty, wait_for_miner_start):
    web3 = web3_ipc_empty

    hashrate = web3.miner.hashrate
    assert hashrate > 0
