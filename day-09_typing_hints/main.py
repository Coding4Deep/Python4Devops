"""This module maps admin users to their assigned ports."""

from typing import Set, List


# Global configuration for admin users and their allowed ports
ADMIN_USERS: Set[str] = {"alice", "bob", "charlie"}
PORTS: Set[int] = {80, 8080, 3000}


def valid_admin(users: Set[str], port_numbers: Set[int]) -> List[str]:
    """Return a list combining each admin user with a port number.

    Args:
        users (Set[str]): A set of admin usernames.
        port_numbers (Set[int]): A set of allowed ports.

    Returns:
        List[str]: A list of strings combining username and port.
    """
    return [f"{user}:{port}" for user, port in zip(users, port_numbers)]


if __name__ == "__main__":
    print(valid_admin(ADMIN_USERS, PORTS))
