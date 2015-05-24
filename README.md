# csfdranks  

Command-line tool to work with rankings of ČSFD.

## usage

csfdranks [-h] [--source_type {html}] [-s {order,film,average,count,rating}] [-o {simple,stats}] source  

positional arguments:  
  source - the data source  

optional arguments:  
  -h, --help - show this help message and exit  
  --source_type {html} - the data source type  
  -s {order,film,average,count,rating}, --sort_by {order,film,average,count,rating} - the key for sorting output  
  -o {simple,stats}, --output_type {simple,stats} - the type of the output  

## requirements

python2.7 and the following packages  
BeautifulSoup

