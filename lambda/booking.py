import json
import boto3
import os
from datetime import datetime

def lambda_handler(event, context):
    # Parse booking data from form
    body = json.loads(event.get('body', '{}'))
    
    name    = body.get('name', 'Unknown')
    email   = body.get('email', 'Unknown')
    phone   = body.get('phone', 'Unknown')
    date    = body.get('date', 'Unknown')
    guests  = body.get('guests', 'Unknown')
    message = body.get('message', 'No message')
    
    # Send email via SES
    ses = boto3.client('ses', region_name='us-east-1')
    
    ses.send_email(
        Source='ayudh165@gmail.com',
        Destination={
            'ToAddresses': ['ayudh165@gmail.com']
        },
        Message={
            'Subject': {
                'Data': f'🌿 New Panchase Booking from {name}'
            },
            'Body': {
                'Text': {
                    'Data': f'''
New Booking Request - Panchase Eco Tourism

Name:    {name}
Email:   {email}
Phone:   {phone}
Date:    {date}
Guests:  {guests}
Message: {message}

Received: {datetime.now().strftime("%Y-%m-%d %Human:%M:%S")}
                    '''
                }
            }
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
        },
        'body': json.dumps({'message': 'Booking received! We will contact you soon.'})
    }