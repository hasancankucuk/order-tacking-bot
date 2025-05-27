from app import generate_fake_data
from db import db_utils
from scripts import (
    generate_nlu,
    generate_domain,
    generate_rules,
    generate_stories,
    generate_config,
    generate_credentials,
    generate_endpoints,
    doppler_env,
)
import os
from dotenv import load_dotenv


def run_all():
    try:
        doppler_env.main()
        load_dotenv(override=True)
        
        db_utils.create_db()
        
        generate_nlu.main()
        generate_domain.main()
        generate_rules.main()
        generate_stories.main()
        generate_config.main()
        generate_credentials.main()
        generate_endpoints.main()
        
        print("Setup completed successfully!")
        
    except Exception as e:
        print(f"Error during setup: {e}")
        raise


if __name__ == "__main__":
    run_all()
    
