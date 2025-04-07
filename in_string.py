def check_vowels():
    # Código a implementar utilizando input.
    name = input("Ingrese su nombre: ")
    valor = name.lower()
    
    print(f"Contiene a: {"a" in valor}")
    print(f"Contiene e: {"e" in valor}")
    print(f"Contiene i: {"i" in valor}")
    print(f"Contiene o: {"o" in valor}")
    print(f"Contiene u: {"u" in valor}")


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
