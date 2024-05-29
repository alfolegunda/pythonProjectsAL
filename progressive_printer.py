import time

def progressive_print(text, delay=0.01, repetitions=10):
    for i in range(1, len(text) + 1):
        # Genera la parte del texto a imprimir
        partial_text = text[:i]
        # Repite la impresión del texto parcial
        for _ in range(repetitions):
            print(partial_text)
            time.sleep(delay)

txt = "Hello World"
progressive_print(txt)