#!/bin/bash
set -e

sudo apt update
sudo apt install -y python3-pip python3-venv nats-server ros-humble-desktop ros-dev-tools

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install pydantic openai anthropic python-dotenv nats-py rclpy opencv-python matplotlib

echo "Dependencies installed."
chmod +x launch.sh
