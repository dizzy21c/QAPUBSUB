from QAPUBSUB import consumer
import json

c = consumer.subscriber_routing(exchange='QARealtime_Market', routing_key='0')
# c = consumer.subscriber(exchange='ctp')
def callback(a, b, c, data):
    data = json.loads(data)
    print(data)
    if data['topic'] == 'subscribe':
        print('receive new subscribe: {}'.format(data['code']))
        new_ins = data['code'].replace('_', '.').split(',')

        import copy
        if isinstance(new_ins, list):
            for item in new_ins:
                print(item)
                # self.subscribe(item)
    #     else:
    #         self.subscribe(new_ins)
    # if data['topic'] == 'unsubscribe':
    #     print('receive new unsubscribe: {}'.format(data['code']))
    #     new_ins = data['code'].replace('_', '.').split(',')

    #     import copy
    #     if isinstance(new_ins, list):
    #         for item in new_ins:
    #             self.unsubscribe(item)
    #     else:
    #         self.unsubscribe(new_ins)
c.callback = callback
c.start()
