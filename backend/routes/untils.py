import bcrypt

def hashFunction(password:str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# def veryfy_password(self, plain_password: str) -> bool:
#     return bcrypt.checkpw(
#         plain_password.encode('utf-8'),
#         self.hashed_password.encode('utf-8')
#     )
    