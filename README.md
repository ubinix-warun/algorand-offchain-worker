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
offchain creator account: VJ5FDKF3I5TD3WBMNQS4UCNUNF6DBWKJI3PCSMTWQOJXBRMGVHSIF2MLQ4
Done. The OffChain app ID is 234 

```

# Notes

![PT2](https://raw.githubusercontent.com/ubinix-warun/algorand-offchain-worker/main/doc/assets/proto_indexer2.png)

