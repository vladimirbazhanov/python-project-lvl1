from brain_games.shared import welcome_user, get_username, greet_user


def main():
    welcome_user()
    username = get_username()
    greet_user(username)


if __name__ == '__main__':
    main()
