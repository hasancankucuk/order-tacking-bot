import os
import textwrap
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

def main():
    webhook_url = os.getenv('WEBHOOK')
    
    endpoints_content = textwrap.dedent(f"""\
        action_endpoint:
          url: "{webhook_url}"
    """)

    with open("endpoints.yml", "w", encoding="utf-8") as f:
        f.write(endpoints_content)