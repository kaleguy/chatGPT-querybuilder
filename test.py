import requests

# Replace 'your_api_key' with your actual API key
api_key = ''
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    'model': 'gpt-3.5-turbo',
    'messages': [
        {'role': 'user', 'content': 'Hello, how are you?'}
    ]
}

response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
print(response.json())
