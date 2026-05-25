# =====================================================================
# Curso: Fundamentos de Programación
# Fase 5: Evaluación Final POA
# Estudiante: Javier Andrés Triana Cárdenas
# Problema Seleccionado: Problema 2 - Gestión de Precios de Menú
# =====================================================================

def calcular_precio_final(categoria_producto, precio_base, categoria_objetivo, umbral_precio):
    """
    Función (módulo) para calcular el precio final aplicando la lógica de negocio:
    Aplica 15% de descuento si pertenece a la categoría objetivo y supera el precio umbral.
    """
    # Verificación de condiciones de la promoción
    if categoria_producto.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        # Se mantiene el precio base si no cumple los requisitos
        precio_final = precio_base
        
    return precio_final


def main():
    # R1: Crear la matriz con 6 productos [Nombre, Categoría, Precio Base]
    # Nota: Los precios están expresados en valores decimales/enteros estándar.
    menu = [
        ["Hamburguesa Especial", "Comida Rapida", 25000],
        ["Perro Caliente Simple", "Comida Rapida", 12000],
        ["Pizza Personal", "Comida Rapida", 18000],
        ["Limonada Cerezada", "Bebidas", 8500],
        ["Jugo Natural", "Bebidas", 6000],
        ["Copa de Helado", "Postres", 11000]
    ]
    
    print("=== CONFIGURACIÓN DE LA PROMOCIÓN ===")
    # R2: Definir variables de control para la promoción (pueden ser dinámicas o fijas)
    categoria_objetivo = "Comida Rapida"
    umbral_precio = 15000
    
    print(# Usamos formato markdown simple en texto para la consola
        f"Promoción válida para la categoría: '{categoria_objetivo}' "
        f"con precio base mayor a: ${umbral_precio}\n"
    )
    
    print("=======================================================================")
    print(f"{'PRODUCTO':<25} | {'CATEGORÍA':<15} | {'P. BASE':<10} | {'P. FINAL':<10}")
    print("=======================================================================")
    
    # R5: Recorrer la matriz usando estructuras repetitivas
    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]
        
        # R4: Llamado al módulo/función de cálculo
        precio_final = calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral_precio)
        
        # Mostrar resultados formateados
        print(f"{nombre:<25} | {categoria:<15} | ${precio_base:<9} | ${precio_final:<10.1f}")
        
    print("=======================================================================")

# Punto de entrada del programa estructurado
if __name__ == "__main__":
    main()