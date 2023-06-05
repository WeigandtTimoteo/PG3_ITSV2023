def validate_password(password):
    if len(password) < 8:
        print("La contraseña debe tener al menos 8 caracteres")
        return False
    elif not any(char.isdigit() for char in password):
        print("La contraseña debe contener al menos un número")
        return False
    elif not any(char.isupper() for char in password):
        print("La contraseña debe contener al menos una letra mayúscula")
        return False
    elif not any(char.islower() for char in password):
        print("La contraseña debe contener al menos una letra minúscula")
        return False
    elif any(char in "!@#$%^&*()-+" for char in password):
        print("La contraseña no debe contener un carácter especial")
        return False
    else:
        print("La contraseña es valida")
        return True