from passlib.context import CryptContext

password_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash:
    def bcrypt(password):
        ''' Hashes the normal password. '''
        return password_context.encrypt(password)
    
    def verify_password(entered, original):
        ''' Verifies if entered password matches the hashed password.'''
        return password_context.verify(entered, original)