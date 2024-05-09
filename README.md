# TeleDeployGenerator
# Deployment Script Generator for Telegram bot

This script streamlines the deployment process for services using Docker Compose by automatically generating environment variables and a deployment script. It's designed to cater to the needs of Telegram bot development, ensuring a smooth setup experience.

## Features

- Automatically generates environment variables for MariaDB (MySQL) or PostgreSQL databases, with MariaDB (MySQL) as the default option.
- Constructs a comprehensive deployment script for services, utilizing Docker Compose for seamless integration.

## Prerequisites

- Python 3.x installed on your system.
- Docker and Docker Compose installed and configured.

## Usage

1. **Clone the Repository**: Start by cloning this repository to your local machine.

```bash 
git clone https://github.com/Lacolle87/TeleDeployGenerator.git
```

2. **Navigate to the Project Directory**: Change your current directory to the cloned repository.

```bash 
cd TeleDeployGenerator
```

3. **Prepare the Script**: Make the script executable and move it to a directory in your PATH for easy access.

```bash 
chmod +x main.py 
sudo mv main.py /usr/local/bin/initbot
```

4. **Generate Environment Variables**: Run the script. MariaDB (MySQL) is the default database option. If you prefer PostgreSQL, include the `-p` flag.

```bash 
initbot -p # For PostgreSQL
```
or simply
```bash 
initbot # For MariaDB (MySQL)
```

5. **Follow the Prompts**: The script will guide you through entering the required information. Upon completion, it generates the necessary environment variable files and a deployment script named `deploy_services.sh`.

6. **Deploy Your Services**: Execute the generated deployment script to start your services.

```bash 
bash deploy_services.sh
```

This process automates the initial setup, allowing you to focus on developing and deploying your Telegram bot with ease.
