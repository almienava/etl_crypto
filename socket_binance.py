import websocket
import json
import threading

symbols = ["bnbusdt", "btcusdt","ethusdt"]
def on_message(ws, message):
    data = json.loads(message)

    print(data)
    print("--------------------")
    
def create_websocket(symbol):
    websocket_url = f"wss://stream.binance.com:9443/ws/{symbol}@trade"
    ws = websocket.WebSocketApp(websocket_url, on_message=on_message)
    ws.run_forever()
threads = []

for symbol in symbols:
    thread = threading.Thread(target=create_websocket, args=(symbol,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


"""
{'e': 'trade', 'E': 1693916140253,
 's': 'BNBUSDT', 't': 670260079, 'p': '214.90000000',
   'q': '0.13700000',
   'b': 4806576967, 
   'a': 4806582177, 
   'T': 1693916140253, 
   'm': True,  (entry order book atau tidak, jika iya maka True)
    'M': True}
"""