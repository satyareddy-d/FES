# We read these values from some external file in production



broker_url = 'amqp://'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']

task_routes = {
    'tasks.send_email': 'fes',
}

enable_utc = True
max_retries = 10
