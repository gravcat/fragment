import requests
import argparse

# get data via arguments
parser = argparse.ArgumentParser(description='Aggregate API data for mining services.')
parser.add_argument('--address',
                    dest='miner_address',
                    default='760dF3ddF5A41Cb67867C4CE01Ad327cBaC2cf99',
                    help='Supply mining address')
requiredGroup = parser.add_argument_group('required arguments')
requiredGroup.add_argument('--pool',
                    choices=['ethpool','ethermine'],
                    help='Mining pool to pull statistics from.',
                    required=True)
args = parser.parse_args()

# retrieve data from ethpool/ethermine API
if args.pool == 'ethpool':
    upstream_api_url = "http://ethpool.org/api/miner_new/" + args.miner_address
elif args.pool == 'ethermine':
    upstream_api_url = "https://ethermine.org/api/miner_new/" + args.miner_address

print('MINER ADDRESS SUPPLIED: ' + args.miner_address)
print('POOL DATA URL: ' + upstream_api_url)

r = requests.get(upstream_api_url)

print(r.json())
