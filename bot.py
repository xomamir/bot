from random import choice


class Bot:

    @staticmethod
    def get_random_message():
        try:
            with open('bot.txt', 'r', encoding='utf8') as file:
                commands = (file.readlines())
            print(choice(commands))
        except FileNotFoundError:
            print('Файл с сообщениями не найден')


    @staticmethod
    def add_message():
        message = input()
        if message is not None:
            with open('bot.txt', 'ab') as file:
                file.write((message + '\n').encode('utf8'))
            print('Сообещние добавлено')


bot = Bot()
bot.get_random_message()
bot.add_message()
