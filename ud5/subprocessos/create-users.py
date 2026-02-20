import argparse
import csv
import os
import subprocess

def check_sudo():
    return os.geteuid() == 0

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
    subprocess.run(args, capture_output=True)


def exists_user(username):
    """
    @returns True if user exists; False otherwise
    """
    args = ["id", "-u", username]
    result = subprocess.run(args, capture_output=True)
    return result.returncode == 0


def set_password(username, password):
    chpasswd_line = f"{username}:{password}"
    result = subprocess.run(["chpasswd"], input=chpasswd_line, capture_output=True, text=True)
    return result.returncode == 0

if __name__ == "__main__":
    if not check_sudo():
        print(f"Error: You must have superuser privileges.")
        exit(1)

    parser = create_parser()
    args = parser.parse_args()

    dry_prefix = ""
    if args.dry:
        dry_prefix = "[DRY]: "

    users = load_users(args.path)
    for u in users:
        nom = u["nom"].lower()
        cognoms = u["cognoms"].lower()
        username = f"{nom[0]}{cognoms}"
        password = u["data_naixement"]

        if not exists_user(username):
            if not args.dry:
                create_user(username)
                set_password(username, password)
            print(f"{dry_prefix}User '{username}' created.")
        else:
            print(f"{dry_prefix}User '{username}' already exists. Skipping.")