# algorand-offchain-worker

In my demo, offchain worker will subscribe event from the indexer, feed some-data to algod via TEAL contract.

![PT2](https://raw.githubusercontent.com/ubinix-warun/algorand-offchain-worker/main/doc/assets/proto_indexer2.png)

```
python3 -m venv venv
. venv/bin/activate

pip3 install -r requirements.txt
python3 demo.py 
```