from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
def change_volume(value):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current = volume.GetMasterVolumeLevelScalar()
    try:
        value = int(value)  # Ensure integer input
        new_vol = max(0.0, min(1.0, current + value / 100))  # Adjust by percent
        volume.SetMasterVolumeLevelScalar(new_vol, None)
        return f"Volume set to {int(new_vol * 100)}%"
    except (ValueError, TypeError):
        return "Invalid volume input. Please provide a number (e.g., 10 or -10)."

def change_brightness(value):
    try:
        value = int(value)  # Ensure integer input
        current = sbc.get_brightness(display=0)[0]
        new_brightness = max(0, min(100, current + value))
        sbc.set_brightness(new_brightness)
        return f"Brightness set to {new_brightness}%"
    except (ValueError, TypeError):
        return "Invalid brightness input. Please provide a number (e.g., 20 or -20)."
    except Exception as e:
        return f"Failed to change brightness: {str(e)}"