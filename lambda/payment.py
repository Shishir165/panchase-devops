import json
import boto3
import os
import urllib.request
import urllib.parse

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
        
        amount      = body.get('amount', 0)        # in cents (5000 = $50)
        currency    = body.get('currency', 'usd')
        experience  = body.get('experience', 'Panchase Experience')
        success_url = body.get('success_url', 'https://panchase.com?payment=success')
        cancel_url  = body.get('cancel_url', 'https://panchase.com?payment=cancelled')

        # Get Stripe secret key from environment
        stripe_key = os.environ['STRIPE_SECRET_KEY']

        # Create Stripe checkout session
        data = urllib.parse.urlencode({
            'payment_method_types[]': 'card',
            'line_items[0][price_data][currency]': currency,
            'line_items[0][price_data][product_data][name]': experience,
            'line_items[0][price_data][unit_amount]': str(amount),
            'line_items[0][quantity]': '1',
            'mode': 'payment',
            'success_url': success_url,
            'cancel_url': cancel_url,
        }).encode()

        req = urllib.request.Request(
            'https://api.stripe.com/v1/checkout/sessions',
            data=data,
            headers={
                'Authorization': f'Bearer {stripe_key}',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )

        with urllib.request.urlopen(req) as response:
            session = json.loads(response.read().decode())

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
            },
            'body': json.dumps({
                'checkout_url': session['url'],
                'session_id': session['id']
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
            },
            'body': json.dumps({'error': str(e)})
        }