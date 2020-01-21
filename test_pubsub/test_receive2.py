from QAPUBSUB import consumer
import sys

def test_sub(block_id):
  # block_id = 'udf'
  c = consumer.subscriber_routing(exchange='realtime_block_{}'.format(block_id), routing_key=block_id)
  c.callback = lambda a,b,c,data: print(data)
  c.start()
    
if __name__ == "__main__":
  if len(sys.argv) > 1:
    test_sub(sys.argv[1])
  else:
    test_sub('0')

