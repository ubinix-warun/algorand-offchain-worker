# Algorand Offchain Worker

In my demo, offchain worker will subscribe event from the indexer, feed some-data to algod via TEAL contract.

Inspried by [chainlink-polkadot](https://github.com/smartcontractkit/chainlink-polkadot/tree/master/pallet-chainlink)

### Algorand Challenge: Developer Tooling

![PT2](https://raw.githubusercontent.com/ubinix-warun/algorand-offchain-worker/main/doc/assets/gitcoin_bounties.png)

https://gitcoin.co/issue/algorandfoundation/grow-algorand/132/100027512

# Quickstart

```
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt
python3 demo.py 

Generating temporary accounts...
offchain creator account:  W77HA6WPJBR52RNGXGCKDGIZKSE65F2HJS4XAQ6Y7RQQ6J2TWQQ6CJI2ZA
Done. The OffChain app ID is 594 
and the offchain account is M475MATP7W4BDX35R5PO7VYFE4GO2EYZRBGMSTIFW7UBL3L3T65NKLDONQ 

Request.  get <>  https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD 

 On REQ ... 1s
 On REQ ... 2s
 On REQ ... 3s

```


