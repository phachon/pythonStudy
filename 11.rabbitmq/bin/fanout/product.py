"""
fonout 模式下生产者
@author phachon@163.com
"""
import pika

# 连接服务器
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.30.128', 5672, '/', credentials))

# 创建频道
channel = connection.channel()

# 定义交换机并持久化
channel.exchange_declare(exchange='fanout_exchange',
                         type='fanout',
                         durable=True)

# 将消息发送到交换机,不需要 routing_key, 并将消息持久化
channel.basic_publish(exchange='fanout_exchange',
                      routing_key='',
                      body='fanout Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2,)
                      )

print("fanout模式发送")

# 缓冲区已经flush而且消息已经确认发送到了RabbitMQ中，关闭链接
connection.close()
