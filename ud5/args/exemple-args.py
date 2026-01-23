import argparse

parser = argparse.ArgumentParser(description="Programa d'exemple amb argparse")
parser.add_argument("username", nargs="+")
parser.add_argument("-u", "--upper", action="store_true")
parser.add_argument("-t", "--tag", action="append", default=[])
parser.add_argument("-v", "--verbose", action="count", default=0)
args = parser.parse_args()

print(args)
print("Nom d'usuari:", args.username)