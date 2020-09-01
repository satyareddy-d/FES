# FES
 Fastest Email Service


# --------------------------------------------------------------------------------------------------------

#  The Techstack to build fastest email service
# Language:
    Python 3
# message broker:
     RabbitMQ
# Framwork:
     Celery-4

# Database(optional):
     postgress --> just to audit the emails that we are sending through FES(Fastest email service)



# Idea behind usage of this service?
  ---> client applications will put the messages into rabbitmq queue 'fes' , then rest of the things takes care by FES(sending emails to recipients)
# How do you put the message into 'fes' queue to send notification emails?
  ---> we use rabbitMQ vhost ULR to push the message into queue by using pika module in python
 
