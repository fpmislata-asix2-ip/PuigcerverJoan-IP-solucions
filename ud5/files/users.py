class User:
    def __init__(self, username, uid, gid, shell):
        self.username = username
        self.uid = uid
        self.gid = gid
        self.shell = shell
        self.primary_group = None
        self.secondary_groups = []

    def set_primary_group(self, primary_group):
        self.primary_group = primary_group

    def __repr__(self):
        return f"User(username={self.username}, uid={self.uid})"


class Group:
    def __init__(self, groupname, gid):
        self.groupname = groupname
        self.gid = gid

    def __repr__(self):
        return f"Group(groupname={self.groupname}, gid={self.gid})"


def load_users():
    path = "\\\\wsl.localhost\\Ubuntu\\etc\\passwd"
    users = {}

    with open(path, "r") as f:
        for l in f:
            user_parts = l.strip().split(":")
            username = user_parts[0]
            uid = user_parts[2]
            gid = user_parts[3]
            shell = user_parts[6]
            users[username] = User(username, uid, gid, shell)
    
    return users



def load_groups():
    path = "\\\\wsl.localhost\\Ubuntu\\etc\\group"
    groups = {}

    with open(path, "r") as f:
        for l in f:
            group_parts = l.strip().split(":")
            groupname = group_parts[0]
            gid = group_parts[2]
            groups[gid] = Group(groupname, gid)
    
    return groups


def link_users_primary_group(users, groups):
    for u in users.values():
        primary_group = groups[u.gid]
        u.set_primary_group(primary_group)


if __name__ == "__main__":
    users = load_users()
    groups = load_groups()
    link_users_primary_group(users, groups)

    for u in users.values():
        if u.shell == "/bin/bash":
            print("Username:", u.username)
            print("UID:", u.uid)
            print("Primary group:", u.primary_group)
