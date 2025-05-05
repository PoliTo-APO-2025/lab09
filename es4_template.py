from typing import Container


class SocialNetwork:
    def create_account(self, username: str) -> None:
        pass

    def follow(self, follower: str, followed: str) -> None:
        pass

    def has_account(self, username: str) -> bool:
        pass

    def get_followers(self, username) -> Container[str]:
        pass

    def get_followed(self, username) -> Container[str]:
        pass

    def get_users(self) -> Container[str]:
        pass

    def __len__(self) -> int:
        pass


def main():
    # caricare rete da file e testare metodi
    pass


if __name__ == "__main__":
    main()
