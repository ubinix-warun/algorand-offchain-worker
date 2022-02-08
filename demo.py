from time import time, sleep

from algosdk import account, encoding
from algosdk.logic import get_application_address
# from auction.operations import createOffChainApp

def demo():
    client = getAlgodClient()

    print("Generating temporary accounts...")
    # ---

    appID = createOffChainApp(
        client=client,
        sender=creator
    )
    print(
        "Done. The OffChain app ID is",
        appID,
        "\n",
    )

    # Request Datafeed!

demo()
