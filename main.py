from discord_bot import *
from session_notes import generate_session_notes
import atexit

def main():
    discord_bot()

atexit.register(generate_session_notes)

if __name__ == "__main__":
    main()