# FES
 Fastest Email Service in Dev in Progress
 
# Architecture Diagram


![Alt text](https://github.com/satyareddy-d/FES/blob/master/FES_Architecture.PNG?raw=true "Diagram")


message --> {
    'subject': "some subject",
    'email_body': "some html string",
    'to_addresses': ['abc@gmail.com']
}

---------------------------------------------------------

# Pending Work:
 1) CI/CD pipline through jenkins
 2) Dockerfile
 3) supervisorconfig file to run celery application
 4) unittests
 

# --------------------------------------------------------

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
  
# Open Questions
1) should we use celery eventlet pool insteaded of prefork process as we have to only simple I/O network call?
 
