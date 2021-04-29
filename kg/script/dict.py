import argparse
import json


def get_parser():
    parser = argparse.ArgumentParser(description="Usage: python dict.py -d '' -k 'c'")
    parser.add_argument("--dict", "-d", type=str, required=True, default='', help="Mention Dict")
    parser.add_argument("--key", "-k", type=str, required=True, default='', help="Mention Key")
    return parser

def recursive_loop(k, dt):
    if k in dt.keys():
        return dt[k]
    for v in dt.values():
        if isinstance(v, dict):
            a = recursive_loop(k, v)
            if a is not None:
                return a
    return None

def main(args):
    args.dict = json.loads(args.dict)
    result = recursive_loop(args.key, args.dict)
    print(result)


if __name__ == '__main__':
    ARGS = get_parser().parse_args()
    main(ARGS)