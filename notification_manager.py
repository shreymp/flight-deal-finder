from twilio.rest import Client




class NotificationManager:
    def send_flight_booking_sms(self, message):
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=message,
            from_='+1234412512',
            to='+1122233344'
        )

        print(message.status)
