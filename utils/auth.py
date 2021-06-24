from datetime import datetime,timedelta
import jwt

class TokenProvider:
    def __init__(self):
        self.jwt_time_validity_in_seconds = 7200
        self.secret_key = '#NoSecretKey'

    def provide(self, user_pk):
        try:
            payload = {
                "id":"{}".format(user_pk),
                "exp":datetime.utcnow()+timedelta(seconds=self.jwt_time_validity_in_seconds)
            }
            jwt_token = jwt.encode(payload,self.secret_key)
            return 1, jwt_token

        except:
            return 0, None

    def get_token_value(self, token):
        try:
            decoded_token = jwt.decode(token,self.secret_key)
            user_pk = decoded_token.get('id')
            return True, user_pk
        except:
            return False, None

def authenticate_appuser():
    if 'X-Jwt-Token' in request.headers.keys():
        jwt_token = request.headers.get('X-Jwt-Token').replace('Bearer ','')
        token_provider = TokenProvider()
        sts, user_pk = token_provider.get_token_value(jwt_token)
        return sts, user_pk