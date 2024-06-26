# Telegram Bot with OpenAI Assistant API

This repository contains a Telegram bot that responds to user messages using the OpenAI Assistant API.

## Features

- Responds to user messages with AI-generated responses using the OpenAI Assistant API.

## Prerequisites

- Python 3.6 or higher
- Telegram Bot API token from [BotFather](https://core.telegram.org/bots#botfather)
- OpenAI API key from [OpenAI](https://beta.openai.com/signup/)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/gauravgoyal1/zomadbot
    cd telegram-openai-bot
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your environment variables**:
    Create a `config.json` file in the project directory, using config.json.sample and add your Telegram Bot API token and OpenAI API key:

## Usage

1. **Run the bot**:
    ```sh
    python bot.py
    ```

2. **Interact with the bot on Telegram**:
    - Start the bot by sending `/start`.
    - Send any other message to receive a response generated by the OpenAI Assistant API.

## Files

- `bot.py`: Main script to run the Telegram bot.
- `requirements.txt`: List of required Python packages.

## Dependencies

- `python-telegram-bot`: Python wrapper for the Telegram Bot API.
- `openai`: OpenAI API client library.

## Example

```sh
python bot.py
