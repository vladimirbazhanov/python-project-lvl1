import prompt


def welcome_user():
    print('Welcome to the Brain Games!')


def greet_user(username):
    print(f'Hello, {username}!')


def get_username():
    return prompt.string('May I have your name? ')
