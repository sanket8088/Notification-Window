import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please play dota",
            message="DOTA is a very good game and helps u reduce stress",
            app_icon = "C:/Users/sanke/OneDrive/Desktop/my_project_personal/notification/dota.ico",
            timeout=5
        )
        
        time.sleep(10)