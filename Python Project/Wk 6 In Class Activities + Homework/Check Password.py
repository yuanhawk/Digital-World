def check_password(password):
    num = '0123456789'
    alp = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    if len(password) < 8:
        return False
    for p in password:
        if p not in num:
            if p not in alp:
                return False
        if p in num:
            count += 1
    if count < 2:
        return False
    return True
        