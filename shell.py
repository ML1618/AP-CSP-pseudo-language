import APCSP

while True:
    text = input('APCSP > ')
    result, error = APCSP.run('<stdin>', text)
    
    if error: print(error.as_string())
    elif result: print(result)