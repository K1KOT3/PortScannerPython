import socket
import csv

# Puertos que se comprobarán por defecto
PUERTOS_POR_DEFECTO = [21, 22, 23, 25, 53, 67, 68, 80, 443]

# Función para comprobar si un puerto está abierto
def puerto_abierto(ip, puerto):
    try:
        # Crear un socket de tipo SOCK_STREAM (TCP)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Tiempo de espera en segundos
            if s.connect_ex((ip, puerto)) == 0:  # 0 indica que el puerto está abierto
                return True
    except Exception as e:
        print(f"Error al analizar {ip}:{puerto} - {e}")
    return False

# Leer direcciones IP desde un archivo CSV
def leer_ips_desde_csv(ruta_archivo):
    ips = []
    try:
        with open(ruta_archivo, mode='r') as archivo:
            lector_csv = csv.reader(archivo)
            for fila in lector_csv:
                ips.append(fila[0])  # Leer la primera columna (IP)
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
    return ips

# Guardar los resultados en un archivo CSV
def guardar_resultados(ip, puertos_abiertos):
    archivo_salida = f"{ip}_resultados.csv"
    try:
        with open(archivo_salida, mode='w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(["IP", "Número de puertos abiertos", "Puertos abiertos"])
            escritor_csv.writerow([ip, len(puertos_abiertos), puertos_abiertos])
        print(f"Resultados guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al guardar resultados: {e}")

# Función principal
def principal(archivo_entrada):
    ips = leer_ips_desde_csv(archivo_entrada)
    for ip in ips:
        print(f"Analizando {ip}...")
        puertos_abiertos = []
        for puerto in PUERTOS_POR_DEFECTO:
            if puerto_abierto(ip, puerto):
                puertos_abiertos.append(puerto)
        guardar_resultados(ip, puertos_abiertos)
        print(f"Puertos abiertos para {ip}: {puertos_abiertos}")

# Ejecutar el script
if __name__ == "__main__":
    archivo_ips = "ips.csv"  # Archivo de entrada con direcciones IP
    principal(archivo_ips)
