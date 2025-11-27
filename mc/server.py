import os
import subprocess
import config

from mc.rcon_client import RconClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# General Commands
def get_server_status() -> str:
    with RconClient() as rcon:
        try:
            rcon.command("list")
            return "Server is running."
        except ConnectionRefusedError:
            return "Server is down."

def get_tps() -> str:
    with RconClient() as rcon:
        try:
            response = rcon.command("tps")
            return response
        except ConnectionRefusedError:
            return "Unable to retrieve TPS. Server might be down."

def get_player_list() -> str:
    with RconClient() as rcon:
        try:
            response = rcon.command("list")
            return response
        except ConnectionRefusedError:
            return "Unable to retrieve player list. Server might be down."

def general_status() -> str:
    status = get_server_status()
    tps = get_tps()
    player_list = get_player_list()
    return f"Status: {status}\nTPS: {tps}\nPlayers: {player_list}"

# Admin Commands
def start_server() -> str:
    return find_and_run_server_script(config.SERVER_SCRIPT_DIRECTORY)

def stop_server() -> str:
    with RconClient() as rcon:
        try:
            rcon.command("stop")
            return "Server is stopping..."
        except ConnectionRefusedError:
            return "Unable to stop server. Server might already be down."

def restart_server() -> str:
    stop_message = stop_server()
    start_message = find_and_run_server_script(config.SERVER_SCRIPT_DIRECTORY)
    return f"{stop_message}\n{start_message}"

def find_and_run_server_script(directory: str) -> str:
    try:
        # List all files in the directory
        files = os.listdir(directory)

        # Look for .sh or .bat files
        for file in files:
            if file.endswith(".sh") or file.endswith(".bat"):
                script_path = os.path.join(directory, file)

                # Run the script
                if file.endswith(".sh"):
                    subprocess.run(["bash", script_path], check=True)
                elif file.endswith(".bat"):
                    subprocess.run([script_path], shell=True, check=True)

                return f"Successfully ran server script: {file}"

        return "No .sh or .bat file found in the directory."

    except Exception as e:
        return f"Failed to run server script: {e}"