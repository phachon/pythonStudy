"""
direct 模式消费
"""
import pika

# 连接
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.30.128', 5672, '/', credentials))

# 创建频道
channel = connection.channel()

exchange = 'direct_exchange'
type = 'direct'
durable = True
routing_key = 'direct_key'

# 定义交换机，进行exchange声明，exchange表示交换机名称，type表示类型
channel.exchange_declare(exchange=exchange,
                         type=type,
                         durable=durable)

# 随机创建队列, exclusive=True表示建立临时队列，当consumer关闭后，该队列就会被删除
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

# 将随机队列与exchange进行绑定
channel.queue_bind(exchange=exchange,
                   queue=queue_name,
                   routing_key=routing_key)

def callback(ch, method, properties, body):
    """ 回调函数,处理从rabbitmq中取出的消息 """

    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
