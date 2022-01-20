# ExMon

exmon can monitor your script and forward exceptions to specified services
- super easy
- modular

# Example

```python

from exmon import ExMon
from exmon.services import Alerta
from exmon.services import DiscordWebhook

# set up discord webhook
discord = DiscordWebhook('<URL>')

# set up alerta
alerta = Alerta(host_url='<HOST_URL>', api_key='<API_KEY>')

# start up ex mon with both services
ExMon(services=[discord, alerta])

# raise test exception
raise Exception('Totally unexpected exception')

```

# Build Information

1. Generate distribution archives: ``python -m build``

2. Uploade distribution archives: ``python3 -m twine upload dist/*``

3. Install and test the package: ``python3 -m pip install --upgrade exmon``

## Useful build links
- https://packaging.python.org/en/latest/tutorials/packaging-projects/
- https://setuptools.pypa.io/en/latest/userguide/declarative_config.html
- https://setuptools.pypa.io/en/latest/userguide/development_mode.html

# TODO

1. more logging