"""doi_prefix_info

Returns information about registartion agency / datacenter for
Datacite prefixes.


Usage:
  doi_prefix_info <prefix>
  doi_prefix_info -h

"""
import sys
from docopt import docopt
import requests
from pprint import pprint

# endpoint = "https://api.datacite.org/dois/"
endpoint = "https://api.datacite.org/"
headers = {'accept': 'application/vnd.api+json'}

def main():
    args=docopt(__doc__, argv=sys.argv[1:], help=True)
    _prefixinfo(args['<prefix>'])

def _prefixinfo(prefix):
    url = endpoint + 'client-prefixes?prefix-id=' + prefix
    resp = requests.get(url, headers=headers)
    resp = resp.json().get('included')
    nodois =  _get_no_dois(resp[0])
    _report(resp, nodois)
   
def _get_no_dois(prefixinfo):
    clientid = prefixinfo.get('id')
    url = endpoint + 'dois?client-id=' + clientid
    resp = requests.get(url, headers=headers)
    nodois = resp.json().get('meta').get('total')
    return nodois

def _report(resp, nodois):
    pprint(resp[0])
    print('No of DOIs: {}'.format(nodois))

if __name__ == "__main__":
    main()
    


