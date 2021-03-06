"""
Example of obtaining a list of statistical information
about the lemma "test" limited to verbs in present tense
(eg "test" and "tests" but not "tested").

"""

import os
import requests
from pprint import pprint

# TODO: replace with your own credentials
app_id, app_key = os.environ['app_id'], os.environ['app_key']
url = 'https://od-api.oxforddictionaries.com/api/v1/stats/frequency/words/en/'

if __name__ == '__main__':
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key},
                     params={
                         'lemma': 'test',
                         'lexicalCategory': 'verb',
                         'grammaticalFeatures': 'tenseType: present',
                     })
    pprint(r.json() if r.status_code == 200 else r.text)
