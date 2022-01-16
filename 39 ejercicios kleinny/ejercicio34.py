#Escribir la función titulo(), la cual recibe un string y lo retorna convirtiendo la primera letra de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados los demás caracteres. Precondición: el separador de palabras es el espacio: " ". Agregar doctests con suficientes casos de prueba para validar que la función retorna el valor esperado ante distintos argumentos.


def titulo(cadena):
    '''
    Recibe una cadena de caracteres y retorna una copia que tiene la
    primera letra de cada palabra en mayúsculas y el resto de las letras
    en minúsculas.
    >>> titulo('esto es una frase')
    'Esto Es Una Frase'
    >>> titulo('ESTO ES UNA FRASE')
    'Esto Es Una Frase'
    >>> titulo('palabra')
    'Palabra'
    >>> titulo('   esto es una frase')
    '   Esto Es Una Frase'
    >>> titulo('esto es una frase   ')
    'Esto Es Una Frase   '
    >>> titulo('esto   es   una   frase')
    'Esto   Es   Una   Frase'
    >>> titulo('')
    ''
    >>> titulo(' ')
    ' '
    >>> titulo('123')
    '123'
    >>> titulo('-1esto 2es 3una 4frase')
    '-1Esto 2Es 3Una 4Frase'
    >>> titulo('esto1 es2 una3 frase4---')
    'Esto1 Es2 Una3 Frase4---'
    '''
    nueva=""
    inicioPalabra_kmdt=True              #indica el inicio de una palabra
    for caracter_kmdt in cadena:
        if not caracter_kmdt.isalpha():
            nueva=nueva+caracter_kmdt
            inicioPalabra_kmdt=True
        else:
            if inicioPalabra_kmdt:
                nueva=nueva+caracter_kmdt.upper()
                inicioPalabra_kmdt=False  #ya no es el inicio de una palabra 
            else:
                nueva=nueva+caracter_kmdt.lower()
    return nueva