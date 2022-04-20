##importa sql ♥
import sqlite3

##crea base de datos ♥
palabras = sqlite3.connect('wordle.db')

## maensajito de espera ♥
print ("CARGANDO...")

##crea tabla ♥
palabras.execute('''CREATE TABLE IF NOT EXISTS palabras (palabra TEXT NOT NULL UNIQUE,
    dificultad TEXT NOT NULL);''')

##crea palabras ♥
respuestas=["pato","pata","cola","nasa","mesa","sopa","gato","lata","mazo","taza","caras","banco","carta","mundo","mural","pizza","freir","audio","papas","razon","mango","brazos","bufon","piedra","grillo","lamina","muñeca","hombro","trueno","flecha"]

## borra datos para evitar errores ♥
palabras.execute("DELETE FROM palabras")
palabras.commit()

##inserta datos ♥
i=0
for i in range (len(respuestas)):
    if len(respuestas[i])==4:
        palabras.execute(f"INSERT INTO palabras (palabra, dificultad) VALUES ('{respuestas[i]}', 'F')")
    elif len(respuestas[i])==5:
        palabras.execute(f"INSERT INTO palabras (palabra, dificultad) VALUES ('{respuestas[i]}', 'M')")
    else:
        palabras.execute(f"INSERT INTO palabras (palabra, dificultad) VALUES ('{respuestas[i]}', 'D')")
    palabras.commit()

## elige palabras ♥
pF = palabras.execute("SELECT palabra FROM palabras WHERE dificultad='F' ORDER BY RANDOM() LIMIT 1").fetchone()[0]
pM = palabras.execute("SELECT palabra FROM palabras WHERE dificultad='M' ORDER BY RANDOM() LIMIT 1").fetchone()[0]
pD = palabras.execute("SELECT palabra FROM palabras WHERE dificultad='D' ORDER BY RANDOM() LIMIT 1").fetchone()[0]