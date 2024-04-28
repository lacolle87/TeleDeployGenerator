#!/usr/bin/env python3
import os


def create_env_file(dir_name, superuser_id):
    env_file_path = os.path.join(dir_name, "env", ".env")

    try:
        os.makedirs(os.path.dirname(env_file_path), exist_ok=True)

        if not os.path.exists(env_file_path):
            with open(env_file_path, "w") as env_file:
                env_file.write(
                    f"TELEGRAM_BOT_TOKEN=\n"
                    f"SUPERUSER_ID={superuser_id}\n"
                    f"DEVMODE=false\n"
                    f"TZ=Europe/Moscow\n"
                    f"MYSQL_USER=\n"
                    f"MYSQL_PASSWORD=\n"
                    f"MYSQL_ROOT_PASSWORD=\n"
                    f"DB_HOST=\n"
                    f"DB_PORT=\n"
                    f"MYSQL_DATABASE=\n"
                )
            print(f"Created {env_file_path}")
        else:
            print(f"Env file already exists at {env_file_path}")

    except OSError as e:
        print(f"Error: {e}")


def main():
    path_names = input("Enter path names separated by commas: ").split(",")
    superuser_id = input("Enter superuser id: ")

    for path_name in path_names:
        dir_name = path_name.strip()
        create_env_file(dir_name, superuser_id)

    print("Everything is set up.")


if __name__ == "__main__":
    main()
