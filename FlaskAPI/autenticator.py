from functools import wraps
import jwt
from flask import  jsonify

def jwt_verificar(token):
    
        try:
            decode = jwt.decode(token,options={"verify_signature": False})
            current_user = Usuario.query.get(decode['id'])
        except:
            return jsonify({"Error": "Invalid or expired token"}), 403
        