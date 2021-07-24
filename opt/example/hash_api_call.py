import sys
import requests

def api_call(hash):
    url = "http://endpoint.com/api/hash"
    p = {"q" : hash}
    r = requests.get(url,params=p)
    print(r.json()["hash"])

def main(argv):
    args = sys.argv
    api_call(args[1])

if __name__ == '__main__':
    main(sys.argv[1:])