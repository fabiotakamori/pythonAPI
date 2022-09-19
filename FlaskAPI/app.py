import json
import datetime
import jwt
from urllib import response
from flask import Flask, Response, request, jsonify
from models.models import Usuario , app
from autenticator import jwt_verificar


def gera_response(status, nome_conteudo,conteudo, mensagem=False):

    body = {}
    body[nome_conteudo] = conteudo
    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="aplication/json")



@app.route("/users/website", methods=["GET"])

def selecionar_usuarios():

    if 'access_token' in request.headers:
            token = request.headers["access_token"]
            jwt_verificar(token)
    else:
            return gera_response(401, "Error", {"name":"Invalid or expired token", "code":"401"})

    usuarios_objetos = Usuario.query.with_entities(Usuario.website).all()
    usuarios_json = [{"website":usuario.website} for usuario in usuarios_objetos]

    return gera_response(200, "Users", usuarios_json)

#texto no nome
@app.route("/users", methods=["GET"])

def selecionar_usuario():

    if 'access_token' in request.headers:
            token = request.headers["access_token"]
            jwt_verificar(token)
    else:
            return gera_response(401, "Error", {"name":"Invalid or expired token", "code":"401"})

    if(request.args.get('nome')==""):

        return gera_response(404, "Error", {"name":"User name not found", "code":"404"})

    usuarios_objetos = Usuario.query.with_entities(Usuario.id, Usuario.nome).filter(Usuario.nome.like('%'+str(request.args.get('nome'))+'%')).all()
    if(len(usuarios_objetos) == 0):

       return gera_response(404, "Error", {"name":"User name not found", "code":"404"})

    usuarios_json = [{"id":usuario.id, "name":usuario.nome} for usuario in usuarios_objetos]

    return gera_response(200, "Users", usuarios_json)
    
#detalhes do usuario
@app.route("/users/detail", methods=["GET"])

def detalhar_usuario():

    if 'access_token' in request.headers:
            token = request.headers["access_token"]
            jwt_verificar(token)
    else:
            return gera_response(401, "Error",{"name":"Unauthorized access", "code":"401"})

    usuarios_objetos = Usuario.query.order_by(Usuario.nome).with_entities(Usuario.nome, Usuario.email, Usuario.company).all()
    usuarios_json = [{"name":usuario.nome, "email":usuario.email, "company":usuario.company} for usuario in usuarios_objetos]

    return gera_response(200, "Users", usuarios_json)

#Gerar token
@app.route('/user/auth', methods=["POST"])

def login():
    
    try:
        user_m = request.json['email']
        user = Usuario.query.filter_by(email=user_m).first()
        if(user == None):
             return gera_response(404, "Error", {"name":"User not found", "code":"404"})
        else:
            payload ={
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'])
            return gera_response(200, "access_token", token)

    except:

        return gera_response(400, "Error", {"name":"Check email and password", "code":"400"})
        
app.run()
