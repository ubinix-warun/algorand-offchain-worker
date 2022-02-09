from time import time, sleep

import threading
import websocket
import socket

from algosdk import account, encoding
from algosdk.logic import get_application_address
from offchain.operations import (
    createOffChainApp,
    waitOffChainAppReadyToRequest,
    requestDataFeed,
)

from offchain.testing.setup import getAlgodClient
from offchain.testing.resources import (
    getTemporaryAccount,
)


def sub_on_message(wsapp, message):
    print(message)
    # print("<>")

def sub_on_error(ws, error):
    print(error)

def sub_on_close(ws, close_status_code, close_msg):
    print("### closed ###")

def sub_on_open(ws):
    print("Opened connection")

def subscriber(name):
    wsapp = websocket.WebSocketApp("ws://localhost:1323/ws", 
                              on_open=sub_on_open,
                              on_message=sub_on_message,
                              on_error=sub_on_error,
                              on_close=sub_on_close)
    wsapp.run_forever(sockopt=((socket.IPPROTO_TCP, socket.TCP_NODELAY,1),))

def demo():
    client = getAlgodClient()

    print("Generating temporary accounts...")
    creator = getTemporaryAccount(client)

    print("offchain creator account: ", creator.getAddress())

    # subscriber.py <appID, creator, client>
    x = threading.Thread(target=subscriber, args=(1,))
    x.start()

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

    waitOffChainAppReadyToRequest(
        client=client,
        appID=appID,
        timeout = 10,
    )
    
    requestDataFeed(
        client=client,
        operator=creator,
        appID=appID,
        method=b"get",
        url=b"https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD",
    )

    waitOffChainAppReadyToRequest(
        client=client,
        appID=appID,
        timeout = 10,
    )
    
demo()


# Concat(Bytes("[\""), Bytes("get"), Bytes("\",\""))
# ["get","https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000"]
# let parameters = ("get", "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=ETH&tsyms=USD", "path", "RAW.ETH.USD.PRICE", "times", "100000000");
