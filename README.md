# Algorand Offchain Worker

In my demo, offchain worker will subscribe event from the indexer, feed data to algod via TEAL contract.

* [The Indexer](https://github.com/ubinix-warun/algorand-indexer) /develop-pub, support pubsub service and publish block.ApplyData to subscriber.
* [The Sandbox](https://github.com/ubinix-warun/algorand-sandbox) /develop-pub, config dockerfile for my indexer and ready to run offchain contract.
* [Offchain Worker](https://github.com/ubinix-warun/algorand-offchain-worker) setup offchain contract and operator.

**the project is not audited and should not be used in a production environment.

Inspried by [chainlink-polkadot](https://github.com/smartcontractkit/chainlink-polkadot/tree/master/pallet-chainlink) and [MIT LICENSE](https://github.com/ubinix-warun/algorand-offchain-worker/blob/master/LICENSE)


### Algorand Challenge: Developer Tooling

![PT2](https://raw.githubusercontent.com/ubinix-warun/algorand-offchain-worker/main/doc/assets/gitcoin_bounties.png)

https://gitcoin.co/issue/algorandfoundation/grow-algorand/132/100027512


### [Sandbox up & Demo.py](https://www.youtube.com/watch?v=LEt7SXV76z0)

# Quickstart

* Create sandbox docker, algod and indexer.

```
./sandbox up -v
Pulling sandbox... (POC: Pubsub Event)
...
Checkout sandbox... (Branch: Pubsub Event)
Branch 'develop-pub' set up to track remote branch 'develop-pub' from 'origin'.
Switched to a new branch 'develop-pub'
...

algod version
12885032963
3.2.3.stable [rel/stable] (commit #d2289a52)
go-algorand is licensed with AGPLv3.0
source code available at https://github.com/algorand/go-algorand

Indexer version
2.8.0-dev.unknown compiled at 2022-02-10T10:17:02+0000 
    from git hash 94894866ce238f157ee416c83b6cd6c4b61bf6f0 (modified)

Postgres version
postgres (PostgreSQL) 13.5
...

```

* Setup python env.

```
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt
```

* Run demo script.

```
python3 demo.py 

Generating temporary accounts...
offchain creator account:  NCA5LCK7HQD35PNEMACJ2M76KPTGWWDEAXHPPATB7LCVOIM5QVSCLZVEAU
Done. The OffChain app ID is 17 
and the offchain account is QUT2ZXGAS7AGEW2Z5OIXRK2WZNLZ3FZMWMJDRAN7ESRI32U67SLYB3HDXE 

Subscriber's connected to ws://localhost:1323/ws 

Call "get ETH/USD price" to Offchain Contract.

Operator state [ NULL => REQ ] at counter= 1s
Operator state [ REQ => INPRG ] at counter= 12s
Operator sending ... 
 http request 
   method= get 
   url= https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD 
   path= RAW.ETH.USD.PRICE
Operator state [ INPRG => DONE ] at counter= 20s
Operator's stored (respdata)

On-chain ETH/USD price is b'3252.92'

```


# Credit

* [Algorand](https://developer.algorand.org/) - Building trusted infrastructure for the Borderless economy. 
* [PyTEAL](https://developer.algorand.org/docs/get-details/dapps/pyteal/) - The python library for generating TEAL programs that provides a convenient and familiar syntax.
* [chainlink-polkadot](https://github.com/smartcontractkit/chainlink-polkadot/tree/master/pallet-chainlink) - This pallet allows your substrate built parachain/blockchain to interract with chainlink. 
* [auction-demo](https://github.com/algorand/auction-demo/) - This demo is an on-chain NFT auction using smart contracts on the Algorand blockchain.

