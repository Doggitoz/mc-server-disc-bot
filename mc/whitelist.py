from mc.rcon_client import RconClient

def add_player(username: str) -> str:
    try:
        with RconClient() as rcon:
            rcon.command(f"whitelist add {username}")
        print("Player added successfully.")
    except Exception as e:
        return f"Failed to add player: {e}"