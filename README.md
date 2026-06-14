# Payment Checker API

This API wraps various payment checker scripts into a unified REST interface.

## Deployment

This project is designed to be deployed on **Railway** or any other platform supporting Python.

## API Usage

All checkers are accessible via:
`GET /api/{checker_name}?str=CC|MM|YY|CVV`

### Available Checkers:
- `braintree_payjustion`
- `braintree_chegd`
- `otropayflow`
- `payflow_pro`
- `payflowchgr`
- `payflowpb`
- `paypal1`
- `stripe_auth2`
- `stripe3`
- `stripe4`
- `stripeautmass`
- `avspfw`
- `braintree`
- `braintree_bueno`
- `braintree_malo`

### Example:
`https://your-app.up.railway.app/api/stripe4?str=4111111111111111|12|2025|123`

## Requirements
The API requires several Python packages which are listed in `requirements.txt`.
