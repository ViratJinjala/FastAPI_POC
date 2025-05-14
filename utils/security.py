from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"]) # bcrypt is hashing algorithm 

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(stored_password: str, new_password: str):
    return pwd_context.verify(new_password, stored_password)