import random
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
puntos = 0
# El usuario deberá contestar 3 preguntas
# Creó una lista en base a las 3 listas con zip y elijo un índice común para cada una de ellas y así tengan una relación entre sí
questions_to_ask = random.choices(list(zip(questions, answers, correct_answers_index)), k=3)
for question, answer, correct_answers in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    index = questions.index(question)
    for i, answer in enumerate(answers[index]):
        print(f"{i + 1}. {answer}")
        # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica que sea un entero dentro del rango de respuestas
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= 4):
            print("Respuesta no valida")
            exit(1)
        # Se verifica si la respuesta es correcta
        user_answer = int(user_answer) - 1
        if user_answer == correct_answers:
            print("¡Correcto!")
            puntos += 1
            break
        else:
            # Si el usuario no responde correctamente después de 2 intentos,
            # se muestra la respuesta correcta
            print(f"Incorrecto. La respuesta correcta es: {correct_answers + 1}")
            puntos -= 0.5
        # Se imprime un blanco al final de la pregunta
    print()
print(f"Puntuación final: {puntos}")