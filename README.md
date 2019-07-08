# doi_prefix_info

Retrieves some information about the registering datacenter from the
[DataCite](https://datacite.org/)
[REST-API](https://support.datacite.org/reference/introduction) for
DataCite supplied prefixes.

**Requires Python 3**

## Usage

    doi_prefix_info <prefix>
    doi_prefix_info -h

## Install

1. Create a virtualenv somewhere and activate it:

   ~~~bash
   virtualenv -p python3 v3
   . v3/bin/activate
   ~~~

2. Install:

   ~~~bash
   pip install git+https://github.com/eawag-rdm/doi_prefix_info.git
   ln -s $(which doi_prefix_info) <execdir>/doi_prefix_info
   ~~~
   where `<execdir>` stands for a directory in your `$PATH`, e.g. `$HOME/bin`

3. Deactivate virtualenv  

   `deactivate`


## Example

	harald@c1$ doi_prefix_info 10.26037
	{'attributes': {'contactEmail': 'doi@library.ethz.ch',
	                'contactName': 'ETH-Bibliothek, Barbara Hirschmann',
	                'created': '2019-06-11T10:58:45.000Z',
	                'description': None,
	                'domains': '*',
	                'hasPassword': True,
	                'isActive': True,
	                'name': 'Uni Genf: Yareta',
	                'symbol': 'ETHZ.GENFYARETA',
	                'updated': '2019-06-11T11:00:43.000Z',
	                'url': 'https://yareta.unige.ch/',
	                'year': 2019},
	 'id': 'ethz.genfyareta',
	 'relationships': {'prefixes': {'data': [{'id': '10.26037',
	                                          'type': 'prefixes'}]},
	                   'provider': {'data': {'id': 'ethz', 'type': 'providers'}}},
	 'type': 'clients'}
	No of DOIs: 12
