import keyboard
import requests

API_KEY = ""
LIMIT = 1


def get_fact() -> dict | None:
    api_url = f"https://api.api-ninjas.com/v1/facts?limit={LIMIT}"
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None


def monitor_keyboard() -> None:
    while True:
        if keyboard.is_pressed("alt+t") or keyboard.is_pressed("alt+y"):
            fact = get_fact()[0].get("fact")
            if fact:
                keyboard.write(fact)
                keyboard.press("enter")


if __name__ == '__main__':
    monitor_keyboard()
