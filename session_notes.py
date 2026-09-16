notes_file = "notes.txt"

def save_notes(local_updated_notes):
    with open(notes_file, "w", encoding="utf-8") as f:
        f.write(local_updated_notes)
    print("Saved session_notes")

def load_notes():
    try:
        with open(notes_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

current_notes = load_notes()

def generate_session_notes():
    from discord_bot import message_history
    from generate_response import generate_response

    updated_notes = generate_response(
    f"""The session is in the process of ending and it's time to edit your notes. 
    This is the Message History:
    {message_history}
    
    Here are your Current Notes:
    {current_notes}
    Your task now is to edit these Notes to let future versions of you remember relevant information. These wont replace your systemprompt, but are a way to store how you feel about certain things, users, etc. and can be seen as a way to store certain information that might be relevant or important in the future.
    You may add/remove as much or as little as you want.
    Just output your updated Notes, nothing else.
    """)
    save_notes(updated_notes)
    return
