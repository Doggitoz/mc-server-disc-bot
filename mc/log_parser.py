import asyncio

async def follow_log(file_path: str):
    """Asynchronously follow a log file and yield new lines as they are added."""
    with open(file_path, 'r') as file:
        # Move to the end of the file
        file.seek(0, 2)
        
        while True:
            line = file.readline()
            if not line:
                await asyncio.sleep(0.1)  # Sleep briefly
                continue
            yield line.strip()