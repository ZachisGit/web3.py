# web3bsc

Python web3 build for the Binance Smart Chain. Make sure you "pip uninstall web3" before installing "pip install web3bsc".
After that you can import web3 into your projects as usual.

```python
import web3

web3.bsc.Bsc(pub_key, priv_key)
w = web3.Web3()     # No middleware injection
                    # No custom HTTPProvider necessary
                    # No finding a BSC-RPC node
                    # No dealing with the right chainID

block = w.eth.getBlock("latest")
print (block)
```

## Get balance of address

```python
import web3

web3.bsc.Bsc(pub_key, priv_key)
w = web3.Web3()

w.eth.getBalance('0x2910543af39aba0cd09dbb2d50200b3e800a63d2');
```

## Github
[https://github.com/ZachisGit/web3bsc]: https://github.com/ZachisGit/web3bsc


## Donations

If you like this project, have the money and want to donate some of your crypto earnings to it:

    Binance Smart Chain: 0x57486D181351145Aa0D69B6C85827FE2CeB83813
