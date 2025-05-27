import os
import textwrap
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

def main():
    rasa_url = os.getenv('RASA_URL')

    credentials_content = textwrap.dedent(f"""\
    rest:
        user_message_evt: user_uttered
        bot_message_evt: bot_uttered
        session_persistence: true
    rasa:
        url: "{rasa_url}"
    """)

    with open('./credentials.yml', 'w') as file:
        file.write(credentials_content)

if __name__ == "__main__":
    main()