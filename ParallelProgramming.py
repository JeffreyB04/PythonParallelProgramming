import threading
import random
import time

def ordena_subvector(subvector, hilo):
    tiempo_inicio = time.time()
    subvector.sort()
    print(subvector)
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    print(f"Hilo {hilo}: Subvector ordenado en (Tiempo: {tiempo_ejecucion} segundos)")

def dividir_vector(vector, num_hilos):
    longitud_subvector = len(vector) // num_hilos
    subvectores = [vector[i:i+longitud_subvector] for i in range(0, len(vector), longitud_subvector)]
    return subvectores

def unir_vectores(subvectores):
    vector_ordenado = [num for subvector in subvectores for num in subvector]
    return vector_ordenado

def ordenar_vector(vector, num_hilos):
    subvectores = dividir_vector(vector, num_hilos)
    threads = []
    for i, subvector in enumerate(subvectores):
        thread = threading.Thread(target=ordena_subvector, args=(subvector, i))
        thread.start()
        threads.append(thread)
        for thread in threads:
            thread.join()
    vector_ordenado = unir_vectores(subvectores)
    vector_ordenado.sort()
    print(f"Vector ordenado final: {vector_ordenado}")

vector_grande = [random.randint(0, 100) for _ in range(100)]

num_hilos = int(input ("Ingrese el número de hilos: "))

ordenar_vector(vector=vector_grande, num_hilos=num_hilos)