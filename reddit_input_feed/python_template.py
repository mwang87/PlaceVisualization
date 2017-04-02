#!/usr/bin/python


import sys
import getopt
import os
import websocket
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        print("Running")
    print("Opened")



def main():
    url = "wss://ws-026b240fd791dec94.wss.redditmedia.com/place?m=AQAAdHvhWPMyLoYqPhSld1t8DJIEblFJtTuOy7oiDQmorgE_UUOG"

    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    main()
