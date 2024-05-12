from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='apiframe',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['requests'],
    description='A Python client for the Apiframe API',
    author='APIFRAME.PRO',
    author_email='hello@apiframe.pro',
    url='https://github.com/yourusername/apiframe-python',
    keywords=['apiframe', 'midjourney client', 'midjourney api', 'api midjourney', 'midjourney ai api', 'midjourney bot api', 'api midjourney api', 'api midjourney bot', 'midjourney api access'],
    long_description=description,
    long_description_content_type="text/markdown"
)
