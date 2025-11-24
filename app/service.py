from app.models import db, User
from sqlalchemy import text
import requests



def list_users():
    users = db.session.execute(text("SELECT * FROM user")).mappings()
    return [dict(row) for row in users]
def create_user_service(name, email):
    if not email or not name:
        return {"error": "Missing 'email' or 'name'"}, 400

    exist_user = db.session.execute(
        text("SELECT * FROM user WHERE email = :email"),
        {"email": email}
    ).fetchone()

    if exist_user:
        return {"error": "User already exist"}, 400

    new_user = User(
        name=name,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "message": "User created successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
    }, 201


def update_user_service(user_id, name, email):
    if not user_id:
        return {"error": "id required"}, 400
    
    if not name and not email:
        return {"error": "empty data"}, 400
    
    user = db.session.execute(
        text("SELECT * FROM user WHERE id = :id"),
        {"id": user_id}
    ).fetchone()
    
    if not user:
        return {"error": "user not found"}, 400
    
    if email:
        existing_email = db.session.execute(
            text("SELECT * FROM user WHERE email = :email AND id != :id"),
            {"email": email, "id": user_id}
        ).fetchone()
        
        if existing_email:
            return {"error": "Email já está em uso por outro usuário"}, 400
    
    user_obj = db.session.get(User, user_id)
    
    if name:
        user_obj.name = name
    if email:
        user_obj.email = email
    
    db.session.commit()
    
    return {
        "message": "user updated successfully",
        "user": {
            "id": user_obj.id,
            "name": user_obj.name,
            "email": user_obj.email
        }
    }, 200


def delete_user_service(user_id):
    if not user_id:
        return {"error": "User ID is required"}, 400
    
    user = db.session.execute(
        text("SELECT * FROM user WHERE id = :id"),
        {"id": user_id}
    ).fetchone()
    
    if not user:
        return {"error": "User not found"}, 404
    
    user_obj = db.session.get(User, user_id)
    
    db.session.delete(user_obj)
    db.session.commit()
    
    return {
        "message": "User deleted successfully"
    }, 200


def get_usd_brl_rate():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            return {"error": "Não foi possível obter a cotação"}, response.status_code
        
        data = response.json()
        
        if "USDBRL" not in data:
            return {"error": "Dados não encontrados"}, 404
        
        exchange_data = data["USDBRL"]
        
        return {
            "code": exchange_data["code"],
            "codein": exchange_data["codein"],
            "name": exchange_data["name"],
            "high": exchange_data["high"],
            "low": exchange_data["low"],
            "varBid": exchange_data["varBid"],
            "pctChange": exchange_data["pctChange"],
            "bid": exchange_data["bid"],
            "ask": exchange_data["ask"],
            "timestamp": exchange_data["timestamp"],
            "create_date": exchange_data["create_date"]
        }, 200
        
    except requests.exceptions.Timeout:
        return {"error": "Timeout ao conectar com a API"}, 504
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao conectar com a API: {str(e)}"}, 503
    except Exception as e:
        return {"error": f"Erro interno: {str(e)}"}, 500

