import urllib3
import argparse

url = "http://169.254.169.254/latest/meta-data/"


parser = argparse.ArgumentParser(description="Usage: python metadata.py -k 'iam/info'")
parser.add_argument("--key", "-k", type=str, required=False, default='', help="Mention Key")
args = parser.parse_args()


if args.key:
    url = url + args.key

http = urllib3.PoolManager()
r = http.request('GET', url)

print(r.data)