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