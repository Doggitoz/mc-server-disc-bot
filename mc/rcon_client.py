from mcrcon import MCRcon
import config

class RconClient:
    def __enter__(self):
        self.conn = MCRcon(
            config.MCRCON_HOST,
            config.MCRCON_PASSWORD, 
            port=config.MCRCON_PORT
        )
        self.conn.connect()
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.disconnect()