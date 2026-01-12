# Tarea: Implementación de Tipos de Datos e Identificadores
# Funcionalidad: Este programa calcula el promedio de temperaturas y 
# determina si el clima es apto para una actividad.

def verificar_clima():
    # Identificadores descriptivos en snake_case
    
    # 1. String (Cadena de texto)
    ciudad = "Quito" 
    
    # 2. Integer (Entero)
    dias_registrados = 3 
    
    # 3. Float (Flotante)
    temperatura_1 = 18.5
    temperatura_2 = 21.0
    temperatura_3 = 15.2
    
    # Cálculo lógico
    promedio = (temperatura_1 + temperatura_2 + temperatura_3) / dias_registrados
    
    # 4. Boolean (Booleano)
    es_clima_calido = promedio > 20.0
    
    # Mostrar resultados
    print(f"Reporte para la ciudad de: {ciudad}")
    print(f"El promedio de temperatura es: {promedio:.2f}°C")
    print(f"¿Es un clima cálido hoy?: {es_clima_calido}")

if __name__ == "__main__":
    verificar_clima()