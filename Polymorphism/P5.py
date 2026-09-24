class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")

class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")

class PushNotification(Notification):
    def send(self):
        print("Sending Push Notification.")

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()