# Escáner de Puertos en Python

Este es un sencillo script en Python que permite analizar puertos abiertos en direcciones IP especificadas en un archivo CSV. El programa utiliza bibliotecas básicas de Python como `socket` y `csv`, sin depender de herramientas externas como Nmap.

## Características

- Escanea puertos comunes: 21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 67/68 (DHCP), 80 (HTTP) y 443 (HTTPS).
- Lee direcciones IP desde un archivo CSV (`ips.csv`).
- Genera un archivo CSV de resultados para cada dirección IP analizada.
- Implementa tiempo de espera para evitar bloqueos durante el escaneo.

## Requisitos

- **Python 3.6 o superior**.
- Un archivo `ips.csv` con una lista de direcciones IP (una por línea).

## Uso

1. Asegúrate de tener el archivo `ips.csv` en el mismo directorio que el script. Un ejemplo del contenido del archivo:
   ```csv
   192.168.1.1
   192.168.1.2
   192.168.1.3
   ```
2. Ejecuta el script desde la terminal:
   ```bash
   python3 programa_puertos.py
   ```
3. Los resultados se guardarán en archivos CSV individuales para cada IP, nombrados como 192.168.1.1_resultados.csv, 192.168.1.2_resultados.csv, etc.

## Ejemplo de salida

El archivo generado contiene información como esta:
 ```bash
   IP,Número de puertos abiertos,Puertos abiertos
   192.168.1.1,3,[22, 80, 443]
   ```

## Mejoras futuras

- Soporte para escanear rangos de puertos personalizados.
- Implementación de escaneo concurrente para mayor velocidad.
- Posibilidad de detectar servicios en los puertos abiertos.

## Notas
Este script está diseñado como una herramienta educativa para entender cómo funcionan los escaneos de puertos y no debe ser utilizado para actividades no autorizadas. Usa esta herramienta únicamente en redes de prueba o con permiso del propietario.

