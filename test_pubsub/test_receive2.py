from QAPUBSUB import consumer

c = consumer.subscriber_routing(exchange='realtime_stock_0', routing_key='0')
c.callback = lambda a,b,c,data: print(data)
c.start()
