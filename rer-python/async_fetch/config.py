import os
import yaml
from urllib.parse import urlencode

def load_yaml_to_env(yaml_file):
    with open(yaml_file, 'r') as f:
        config = yaml.safe_load(f)
        for endpoint in config.items():
            full_url = f"{endpoint[1]['url']}?{urlencode(endpoint[1]['PARAMS'])}"
            os.environ[endpoint[0]] = full_url

if __name__ == '__main__':
    yaml_file = 'config.yaml'
    load_yaml_to_env(yaml_file)
