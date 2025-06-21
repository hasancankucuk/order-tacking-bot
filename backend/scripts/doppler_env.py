from dopplersdk import DopplerSDK
import os

def generate_env_file(access_token: str, project: str, config: str, output_path: str = ".env"):
    doppler = DopplerSDK()
    doppler.set_access_token(access_token)
    print(f"Fetching secrets for project '{project}' / config '{config}'...")

    try:
        response = doppler.secrets.list(project=project, config=config)
        secrets = response.secrets
    except Exception as e:
        print("Failed to fetch secrets:", str(e))
        return

    with open(output_path, "w") as f:
        for key, val in secrets.items():
            f.write(f"{key}={val['raw']}\n")

    print(f".env file created at: {output_path}")


def main():
    ACCESS_TOKEN = "dp.st.dev.mvZ7h5bvWTYOKN0WcvJqdoGXqhAgQLJhEtacYkQ687d"
    PROJECT = "order-tracking-bot"
    CONFIG = "dev"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.dirname(script_dir) 
    project_root = os.path.dirname(backend_dir) 
    frontend_dir = os.path.join(project_root, "frontend")
    
    backend_env_path = os.path.join(backend_dir, ".env")
    print(f"Creating .env file in backend: {backend_env_path}")
    generate_env_file(ACCESS_TOKEN, PROJECT, CONFIG, backend_env_path)
    
    frontend_env_path = os.path.join(frontend_dir, ".env")
    print(f"Creating .env file in frontend: {frontend_env_path}")
    generate_env_file(ACCESS_TOKEN, PROJECT, CONFIG, frontend_env_path)

if __name__ == "__main__":
    main()
