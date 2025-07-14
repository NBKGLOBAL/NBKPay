from twilio.rest import Client

def send_sms(to_number, message):
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_='+YOUR_TWILIO_PHONE_NUMBER',
        to=to_number
    )

# Usage:
# send_sms(user_phone, f"Your NBK Pay payout of {amount} {currency} has been completed. TXN: {txn_id}")