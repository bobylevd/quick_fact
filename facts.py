import keyboard
import requests


def get_fact() -> dict | None:
    api_url = "https://jokesrv.fermyon.app/facts"
    response = requests.get(api_url)
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def monitor_keyboard() -> None:
    while True:
        if keyboard.is_pressed("alt+t") or keyboard.is_pressed("alt+y"):
            fact = get_fact().get("content")
            if fact:
                keyboard.write(fact)
                keyboard.press("enter")


if __name__ == '__main__':
    monitor_keyboard()
