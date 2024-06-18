# Created by XXL-MAN para C1b3rWall2024

import os
import csv

def count_keyword_occurrences(file_path, keywords):
    """
    Cuenta las ocurrencias de palabras clave en un archivo.

    Args:
        file_path (str): Ruta al archivo.
        keywords (list): Lista de palabras clave a buscar.

    Returns:
        int: Número total de ocurrencias de palabras clave en el archivo.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return sum(content.lower().count(keyword.lower()) for keyword in keywords)
    except FileNotFoundError:
        return 0

def search_keywords_in_directory(directory_path, keywords):
    """
    Busca palabras clave en todos los archivos de texto dentro de un directorio.

    Args:
        directory_path (str): Ruta al directorio.
        keywords (list): Lista de palabras clave a buscar.

    Returns:
        list: Lista de tuplas (ruta_del_archivo, conteo_de_palabras_clave).
    """
    result = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                keyword_count = count_keyword_occurrences(file_path, keywords)
                result.append((file_path, keyword_count))
    return result

def write_csv(sorted_result, output_csv):
    """
    Escribe el resultado ordenado en un archivo CSV.

    Args:
        sorted_result (list): Lista de tuplas (ruta_del_archivo, conteo_de_palabras_clave).
        output_csv (str): Ruta al archivo CSV de salida.
    """
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Ruta del Archivo', 'Conteo de Palabras Clave'])
        writer.writerows(sorted_result)

if __name__ == "__main__":
    # Ejemplo de palabras clave y ruta del directorio
    keywords = ['palabra1', 'palabra2', 'palabra3']
    directory_path = '/ruta/a/tu/directorio'

    # Busca palabras clave en el directorio
    result = search_keywords_in_directory(directory_path, keywords)

    # Ordena el resultado por conteo de palabras clave
    sorted_result = sorted(result, key=lambda x: x[1], reverse=True)

    # Escribe el resultado en un archivo CSV
    output_csv = 'conteo_de_palabras.csv'
    write_csv(sorted_result, output_csv)

    print(f"El conteo de palabras se ha guardado en {output_csv}")
