import argparse
import csv
import subprocess

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--dry", action="store_true", default=False)
    return parser


def load_users(user_file_path):
    with open(user_file_path, "r") as f:
        csv_reader = csv.DictReader(f)
        return list(csv_reader)


def create_user(username):
    args = ["useradd", "-m", "-d", f"/home/{username}", "-s", "/bin/bash", username]
    subprocess.run(args)


def set_password(username, password):
    pass

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    users = load_users(args.path)
    for u in users:
        nom = u["nom"].lower()
        cognoms = u["cognoms"].lower()
        username = f"{nom[0]}{cognoms}"
        create_user(username)