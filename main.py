import toml
import vk_api
from pyrogram import Client
from pyrogram import types, filters

while True:
    try:
        with open("config.toml", "r") as config_file:
            print(config_file.read())
            toml.load(config_file.read())
            telegram.start_parsing()
        break

    except(FileNotFoundError):
        with open("config.toml", "w") as config_file:
            print("""TelegramPost2VK - KirMozor <https://github.com/KirMozor>

This utility automatically forwards all posts from Telegram to VK. To start work, you must specify your password and login, it is necessary for the user bot in Telegram. You also need api_id and api_hash, you can get them from this link: https://my.telegram.org/apps
Then you will need to specify a password and login from VK, it is necessary for posting""")

            telegram_api_id = input("\nInput your api id in telegram: ")
            telegram_api_hash = input("Input your api hash in telegram: ")
            telegram_channel_id = input("Input the channel id for parsing: ")

            vk_phone = input("\nInput your number in VK: ")
            vk_password = input("Input your password in VK: ")

            app = Client(
                "telegram_account",
                telegram_api_id,
                telegram_api_hash
            )


            vk_session = vk_api.VkApi(vk_phone, vk_password)
            vk_session.auth()
            vk = vk_session.get_api()

            config_file.write(
'''vk_phone = "{}"
vk_password = "{}"

telegram_api_id = "{}"
telegram_api_hash = "{}"
channel_telegram_id = "{}"'''.format(vk_phone, vk_password, telegram_api_id, telegram_api_hash, telegram_channel_id))
