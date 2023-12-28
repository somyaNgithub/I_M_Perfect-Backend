# token_utils.py
from rest_framework_simplejwt.tokens import AccessToken

def get_user_id_from_token(request):
    authorization_header = request.headers.get('Authorization', '')
    
    try:       
        token = authorization_header.split(' ')[0]     # Extract the token from the Authorization header
        # print(token)
        
        decoded_token = AccessToken(token).payload     # Decode the token to get the payload
        print(decoded_token)
        
        user_id = decoded_token.get('user_id')         # Retrieve the user ID from the payload
        
        return user_id
    
    except Exception as e:
        print(f"Error: {e}")                           # Handle invalid token or other exceptions
        return None