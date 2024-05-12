# apiframe_python
Python library for [APIFRAME.PRO](https://apiframe.pro) (Midjourney API)

API Documentation is available at https://docs.apiframe.pro

Example

```python

from apiframe_python import ApiframeClient

APIFRAME_API_KEY = "" # YOUR API KEY HERE

client = ApiframeClient(APIFRAME_API_KEY)

task = client.imagine("a nice day near a non-active volcano, photorealism, high details, high quality")

print(task)
```