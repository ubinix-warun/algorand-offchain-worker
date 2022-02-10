from time import time, sleep

from algosdk import account, encoding
from algosdk.logic import get_application_address
from offchain.operations import (
    createOffChainApp,
    waitOffChainAppReadyToRequest,
    requestDataFeed,
    ackDataFeed,
    updateDataFeed,
)

import requests
import json
from jsonpath_ng import jsonpath, parse

from offchain.subscriber import (
    subscriber,
    subscriber_run
)

from offchain.testing.setup import getAlgodClient
from offchain.testing.resources import (
    getTemporaryAccount,
)

def demo():
    client = getAlgodClient()

    print("Generating temporary accounts...")
    creator = getTemporaryAccount(client)

    print("offchain creator account: ", creator.getAddress())

    appID = createOffChainApp(
        client=client,
        operator=creator
    )
    print(
        "Done. The OffChain app ID is",
        appID,
        "\nand the offchain account is",
        get_application_address(appID),
        "\n",
    )

    def on_msg_globalstate(gs): # Feeding Func to Algofrom Algorand blockchaind

        if gs['state']['Bytes'] == "REQ":
            if gs['reqm']['Bytes'] == "get":

                ackDataFeed(
                    client=client,
                    operator=creator,
                    appID=appID
                )

                method = gs['reqm']['Bytes']
                url = gs['requrl']['Bytes']
                path = gs['path']['Bytes']

                print("Request to \n   method=",method, 
                                "\n   url=", url, 
                                "\n   path=", path)
                resp = requests.get(url)
                json_data = json.loads(resp.text)

                jsonpath_expr= parse(path)
                price = jsonpath_expr.find(json_data)

                respData = price[0].value # Result data from Offchain Data

                 # Feed data to Algorand blockchain
                updateDataFeed(
                    client=client,
                    operator=creator,
                    appID=appID,
                    respData=bytes(str(respData), 'utf-8'),
                )
                

    subscriber_run("ws://localhost:1323/ws",
                on_msg_globalstate) # Subscribe Event from Algorand blockchain
    
    requestDataFeed(
        client=client,
        operator=creator,
        appID=appID,
        method=b"get",
        url=b"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD",
        path=b"RAW.ETH.USD.PRICE"
    )

    waitOffChainAppReadyToRequest(
        client=client,
        appID=appID,
        timeout = 50,
    )
    
demo()


# Concat(Bytes("[\""), Bytes("get"), Bytes("\",\""))
# ["get","https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000"]
# let parameters = ("get", "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000");
