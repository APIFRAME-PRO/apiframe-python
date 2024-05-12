import requests

class ApiframeClient:
    def __init__(self, api_key, verbose=False):
        self.base_url = 'https://api.apiframe.pro'
        self.api_key = api_key
        self.verbose = verbose

        if not api_key:
            raise ValueError('The api_key is required!')

    def imagine(self, prompt, aspect_ratio='1:1', process_mode='fast', webhook_url=None, webhook_secret=None):
        data = {
            'prompt': prompt,
            'aspect_ratio': aspect_ratio,
            'process_mode': process_mode,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/imagine', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return
