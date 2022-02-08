from time import time, sleep

from algosdk import account, encoding
from algosdk.logic import get_application_address
from offchain.operations import createOffChainApp

from offchain.testing.setup import getAlgodClient
from offchain.testing.resources import (
    getTemporaryAccount,
)

def demo():
    client = getAlgodClient()

    print("Generating temporary accounts...")
    creator = getTemporaryAccount(client)

    print("offchain creator account:", creator.getAddress())

    appID = createOffChainApp(
        client=client,
        operator=creator
    )
    print(
        "Done. The OffChain app ID is",
        appID,
        "\n",
    )

    # Request Datafeed!

demo()


# Concat(Bytes("[\""), Bytes("get"), Bytes("\",\""))
# ["get","https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000"]
# let parameters = ("get", "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000");
