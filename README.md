![](https://github.com/lmeilibr/vtex/workflows/Python%20package/badge.svg)

# VTEX
VTEX API Wrapper for Python

# Example code

You just need to pass your credentials to the Vtex instance,
and fetch the endpoints.

```python
from vtex import Vtex

client = Vtex(account_name, environment, app_key, app_token)
result = client.logistics.get_all_carriers()
js = result.json
status_code = result.status_code
```
result will be the json response from the get_all_carriers request


