import requests
import json

class Api:
    def __init__(self):
        # API URL
        self.api_url = 'https://follow.sale/api/v1'
        # Your API key
        self.api_key = 'OQ7zzHkirfYtxt7LQtvS4ZyTcFngwup2'

    # Add Order
    def add_order(self, data):
        post = {'key': self.api_key, 'action': 'add', **data}
        result = self.connect(post)
        return json.loads(result)

    # Order status
    def status(self, order_id):
        post = {'key': self.api_key, 'action': 'status', 'order': order_id}
        result = self.connect(post)
        return json.loads(result)

    # Order multi status
    def multi_status(self, order_ids):
        post = {'key': self.api_key, 'action': 'status', 'orders': ','.join(map(str, order_ids))}
        result = self.connect(post)
        return json.loads(result)

    # All services
    def services(self):
        post = {'key': self.api_key, 'action': 'services'}
        result = self.connect(post)
        return json.loads(result)

    # Balance
    def balance(self):
        post = {'key': self.api_key, 'action': 'balance'}
        result = self.connect(post)
        return json.loads(result)

    # Connect to panel
    def connect(self, post):
        url = f"{self.api_url}"
        response = requests.get(url, params=post)
        if response.status_code == 200:
            return response.text
        else:
            return json.dumps({'error': f'Request failed with status code {response.status_code}'})

# Examples`
api = Api()

# return all services
services = api.services()

# return user balance
balance = api.balance()

# add order
order_default = api.add_order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100})  # Default
order_custom_comments = api.add_order({'service': 1, 'link': 'http://example.com/test', 'comments': "good pic\ngreat photo\n:)\n;"})  # Custom Comments
order_drip_feed = api.add_order({'service': 1, 'link': 'http://example.com/test', 'quantity': 100, 'runs': 10, 'interval': 60})  # Drip-feed

# return status, charge, remains, start count, order_id
status = api.status(23)

# return orders status, charge, remains, start count, order_id
statuses = api.multi_status([12, 2, 13])

print("Balance:", balance)
print("Order (Default):", order_default)
print("Order (Custom Comments):", order_custom_comments)
print("Order (Drip-feed):", order_drip_feed)
print("Status:", status)
print("Multi Statuses:", statuses)