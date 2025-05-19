from typing import Container


class SocialNetwork:
    def __init__(self):
        self._users = {}

    def create_account(self, username: str) -> None:
        self._users[username] = set()

    def follow(self, follower: str, followed: str) -> None:
        self._users[follower].add(followed)

    def has_account(self, username: str) -> bool:
        return username in self._users

    def get_followers(self, username) -> Container[str]:
        return {u for u in self._users if username in self._users[u]}

    def get_followed(self, username) -> Container[str]:
        return self._users[username]

    def get_users(self) -> Container[str]:
        return [u for u in self._users]

    def __len__(self) -> int:
        return len(self._users)


def main():
    net = SocialNetwork()

    with open("data/social_graph.txt") as f:
        for line in f:
            users = line.strip().split()
            for user in users:
                if not net.has_account(user):
                    net.create_account(user)
            net.follow(users[0], users[1])

    print(net.get_followers("Diego"))
    print(net.get_followed("Diego"))

    print(len(net))

    print(net.get_users())


if __name__ == "__main__":
    main()
