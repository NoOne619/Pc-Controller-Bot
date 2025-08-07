from langchain.tools import tool
from system_commands import change_volume, change_brightness

@tool
def set_volume(value: str) -> str:
    """Adjust system volume by a percentage """
    try:
        return change_volume(int(value))
    except:
        return "Invalid volume value. Please provide a number (e.g., '10' or '-10')."

@tool
def set_brightness(value: str) -> str:
    """Adjust screen brightness by a percentage."""
    try:
        return change_brightness(int(value))
    except:
        return "Invalid brightness value. Please provide a number (e.g., '20' or '-20')."

TOOLS = [set_volume, set_brightness]