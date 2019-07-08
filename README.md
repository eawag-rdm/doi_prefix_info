# doi_prefix_info

Retrieves some information about information about registartion agency
/ datacenter from the [DataCite](https://datacite.org/)
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
