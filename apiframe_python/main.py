import requests

class ApiframeClient:
    def __init__(self, api_key, verbose=False):
        self.base_url = 'https://api.apiframe.pro'
        self.api_key = api_key
        self.verbose = verbose

        if not api_key:
            raise ValueError('The api_key is required!')

    def imagine(self, prompt, aspect_ratio='1:1', process_mode='fast', webhook_url=None, webhook_secret=None):
        """
        Generate an image using a text prompt. This is the /imagine command on Discord.

        Parameters:
        options (dict): The options dictionary.
            prompt (str): The text prompt for Midjourney AI.
            aspect_ratio (str, optional): Aspect ratio for the image. Default is '1:1'.
            process_mode (str, optional): Generation mode to use for the generation. Can be 'fast' or 'turbo'. Default is 'fast'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

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


    def upscale_1x(self, parent_task_id, index, webhook_url=None, webhook_secret=None):

        """
        Upscale one of the 4 generated images by the Imagine endpoint to get a single image.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            index (str): The index of the image to upscale. Can be 1, 2, 3, or 4.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'index': index,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/upscale-1x', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def upscale_alt(self, parent_task_id, type, webhook_url=None, webhook_secret=None):

        """
        The Upscale (Subtle) option doubles the size of your image and keeps details very similar to the original. The Upscale (Creative) option adds details to the image. You need to upscale 1x first.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the image to upscale, obtained from the /upscale-1x request.
            type (str): The type of upscale. Can be 'subtle' or 'creative'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'type': type,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/upscale-alt', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def upscale_highres(self, parent_task_id, type, webhook_url=None, webhook_secret=None):

        """
        Upscale any image to a higher resolution. The image must not be larger than 2048x2048.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the image to upscale.
            type (str): The type of upscale. Can be '2x' or '4x'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'type': type,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/upscale-highres', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def reroll(self, parent_task_id, prompt=None, aspect_ratio='1:1', webhook_url=None, webhook_secret=None):

        """
        Reroll to create new images from a previous Imagine task.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            prompt (str, optional): Prompt for re-drawing. Default is the original prompt from the parent task.
            aspect_ratio (str, optional): Aspect ratio for the image. Default is '1:1'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'aspect_ratio': aspect_ratio,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret, 'prompt': prompt }.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/reroll', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def variations(self, parent_task_id, index, prompt=None, aspect_ratio='1:1', webhook_url=None, webhook_secret=None):

        """
        Create 4 new variations of one of the 4 generated images by the Imagine request.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            index (str): The index of the image to create variations from. Can be 1, 2, 3, 4, 'strong', or 'subtle'.
            prompt (str, optional): Drawing prompt. Default is the prompt from the parent task.
            aspect_ratio (str, optional): Aspect ratio for the image. Default is '1:1'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'index': index,
            'aspect_ratio': aspect_ratio,
            **{key: value for key, value in {'prompt': prompt, 'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/variations', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def inpaint(self, parent_task_id, mask, prompt=None, webhook_url=None, webhook_secret=None):

        """
        Redraw a selected area of an image. You need to upscale 1x first. (Vary Region)

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            mask (str): Base64 encoding of the image corresponding to the selected area.
            prompt (str, optional): Drawing prompt for selected areas.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'mask': mask,
            **{key: value for key, value in {'prompt': prompt, 'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/inpaint', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def outpaint(self, parent_task_id, zoom_ratio, aspect_ratio='1:1', prompt=None, webhook_url=None, webhook_secret=None):

        """
        The outpaint endpoint enlarges an image's canvas beyond its original size while keeping the contents of the original image unchanged. You need to upscale 1x first. (Zoom Out)

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            zoom_ratio (str): Can be 1, 1.5, or 2.
            aspect_ratio (str, optional): Aspect ratio for the image. Default is '1:1'.
            prompt (str, optional): Drawing prompt for new areas.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'zoom_ratio': zoom_ratio,
            'aspect_ratio': aspect_ratio,
            **{key: value for key, value in {'prompt': prompt, 'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/outpaint', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def pan(self, parent_task_id, direction, prompt=None, webhook_url=None, webhook_secret=None):

        """
        Broadens the image canvas in a specific direction, keeping the original content intact and using prompts and the original image as guides for filling the expanded area. You first need to Upscale 1x.

        Parameters:
        options (dict): The options dictionary.
            parent_task_id (str): The task ID of the original task.
            direction (str): Image expansion direction. Can be 'up', 'down', 'left', or 'right'.
            prompt (str, optional): Drawing prompt for new areas.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'parent_task_id': parent_task_id,
            'direction': direction,
            **{key: value for key, value in {'prompt': prompt, 'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/pan', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def describe(self, image_url, process_mode='fast', webhook_url=None, webhook_secret=None):

        """
        Writes four example prompts based on an image you upload. This is the same as using the /describe command in Discord.

        Parameters:
        options (dict): The options dictionary.
            image_url (str): The URL of the image you want to describe. Should be accessible on the Internet.
            process_mode (str, optional): Generation mode to use for the generation. Can be 'fast' or 'turbo'. Default is 'fast'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'image_url': image_url,
            'process_mode': process_mode,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/describe', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def blend(self, image_urls, dimension='square', process_mode='fast', webhook_url=None, webhook_secret=None):

        """
        Blend multiple images into one image.

        Parameters:
        options (dict): The options dictionary.
            image_urls (list of str): The URLs of the images to blend. Min 2, max 5.
            process_mode (str, optional): Generation mode to use for the generation. Can be 'fast' or 'turbo'. Default is 'fast'.
            dimension (str, optional): Can be 'square', 'portrait', or 'landscape'. Default is 'square'.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'image_urls': image_urls,
            'dimension': dimension,
            'process_mode': process_mode,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/blend', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def seed(self, task_id, webhook_url=None, webhook_secret=None):

        """
        Get the seed of a generated image.

        Parameters:
        options (dict): The options dictionary.
            task_id (str): The task_id of the task.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'task_id': task_id,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/seed', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def faceswap(self, target_image_url, swap_image_url, webhook_url=None, webhook_secret=None):

        """
        Swap the face on a target image with the face on a provided image. Each image must contain only one face.

        Parameters:
        options (dict): The options dictionary.
            target_image_url (str): The URL of the image where the face will be swapped.
            swap_image_url (str): The URL of the image where the new face should be taken from.
            webhook_url (str, optional): The final result of this task will be posted at this URL.
            webhook_secret (str, optional): Will be passed as x-webhook-secret in the webhook call headers for authentication.

        Returns:
        dict: A dictionary containing task_id and errors.
            task_id (str): The ID of the task.
            errors (list of dict): A list of errors, where each error is represented as a dictionary with a 'msg' key.
        """

        data = {
            'target_image_url': target_image_url,
            'swap_image_url': swap_image_url,
            **{key: value for key, value in {'webhook_url': webhook_url, 'webhook_secret': webhook_secret}.items() if value is not None}
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/faceswap', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def fetch(self, task_id):

        """
        Get the result/status of a submitted task.

        Parameters:
        options (dict): The options dictionary.
            task_id (str): The task_id of the task.

        Returns:
        Promise[object]: A promise containing the result/status of the task.
        """

        data = {
            'task_id': task_id,
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/fetch', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return


    def fetch_many(self, task_ids):

        """
        Get the results/statuses of multiple tasks using their task_id.

        Parameters:
        options (dict): The options dictionary.
            task_ids (list of str): The task ids of the tasks, min 2 and max 20.

        Returns:
        Promise[list of object]: A promise containing a list of results/statuses of the tasks.
        """

        data = {
            'task_ids': task_ids,
        }

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.post(f'{self.base_url}/fetch-many', json=data, headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return
 

    def account(self):

        """
        Get details about your account: credits remaining, stats, etc..

        Returns:
        Promise[dict]: A promise containing account details.
            email (str): The email associated with the account.
            credits (int): The remaining credits.
            plan (str): The plan of the account.
            next_billing_date (str or None): The next billing date, or None if not applicable.
            total_images (int): The total number of images.
        """

        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json',
        }

        try:
            response = requests.get(f'{self.base_url}/account', headers=headers)
            response_data = response.json()

            if self.verbose:
                print({'response': response_data})

            return response_data
        except Exception as e:
            print('\n[ERROR]', e, '\n')
            return
