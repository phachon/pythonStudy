"""
direct 模式下生产者
@author phachon@163.com
"""
import pika

# 连接服务器
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.30.128', 5672, '/', credentials))

# 创建频道
channel = connection.channel()

exchange = 'direct_exchange'
type = 'direct'
durable = True
routing_key = 'direct_key'

# 定义交换机并持久化
channel.exchange_declare(exchange=exchange,
                         type=type,
                         durable=durable)

# 将消息发送到交换机
channel.basic_publish(exchange=exchange,
                      routing_key=routing_key,
                      body='direct Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2,)
                      )

print("direct模式发送")

# 缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭链接
connection.close()
