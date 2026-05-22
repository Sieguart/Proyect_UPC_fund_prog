# ==============================================================================
# SISTEMA DE FACTURACIÓN – RESTAURANTE PANCHITA
# ==============================================================================

# --- Definir las variables ---

def calcular_igv(subtotal):
    """Calcula el 18% de IGV sobre el consumo total."""
    return subtotal * 0.18


def aplicar_descuento(subtotal, porcentaje_descuento):
    """Aplica un porcentaje de descuento si el cliente califica."""
    return subtotal * (porcentaje_descuento / 100)


def validar_entero(mensaje):
    """Módulo de Validación: Asegura que el usuario ingrese un número entero válido."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un número mayor o igual a cero.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def validar_flotante(mensaje):
    """Módulo de Validación: Asegura que el usuario ingrese un número decimal válido."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("Por favor, ingrese un valor positivo.")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un valor numérico válido.")
#No tocar mas la variables...


# --- Proceso Principal ---
def main():
    print("===============================================")
    print("   SISTEMA DE FACTURACIÓN – RESTAURANTE PANCHITA")
    print("===============================================\n")
    
    # 1. Entradas Iniciales
    num_personas = validar_entero("Ingrese el número de personas en la mesa: ")
    while num_personas <= 0:
        print("Debe haber al menos 1 persona.")
        num_personas = validar_entero("Ingrese el número de personas en la mesa: ")
        
    lista_productos = []
    
    # 2. Ingreso de Pedidos (Bucle while)
    # Permite al mozo seguir agregando platos a una misma cuenta hasta finalizar.
    continuar = "s"
    print("\n--- Registro de Pedidos ---")
    while continuar.lower() == "s":
        nombre_producto = input("Nombre del producto/plato: ")
        cantidad = validar_entero(f"Cantidad de '{nombre_producto}': ")
        precio = validar_flotante(f"Precio unitario de '{nombre_producto}' (S/.): ")
        
        # Guardamos el producto como un diccionario dentro de nuestra lista
        producto = {
            "nombre": nombre_producto,
            "cantidad": cantidad,
            "precio": precio,
            "subtotal_item": cantidad * precio
        }
        lista_productos.append(producto)
        
        continuar = input("\n¿Desea agregar otro producto? (s/n): ")
        while continuar.lower() not in ['s', 'n']:
            continuar = input("Por favor, responda con 's' (sí) o 'n' (no): ")
    #No tocar mas.

    # 3. Calculo Automatico de Subtotales (Bucle for)
    # Recorre la lista de consumos finales para calcular el total acumulado.
    subtotal_total = 0.0
    for prod in lista_productos:
        subtotal_total += prod["subtotal_item"]
        
    # 4. Aplicacion de Descuentos e Impuestos
    porcentaje_desc = validar_flotante("\nIngrese el porcentaje de descuento a aplicar (0 si no aplica): ")
    descuento_aplicado = aplicar_descuento(subtotal_total, porcentaje_desc)
    
    # Base tras el descuento para calcular el IGV
    subtotal_con_descuento = subtotal_total - descuento_aplicado
    igv = calcular_igv(subtotal_con_descuento)
    
    #El total del consumo con impuesto
    total_final = subtotal_con_descuento + igv
    
    # 5. Divisor de cuentas
    monto_por_persona = total_final / num_personas

    # --- Interfaz y Salidas ---
    # Generación de Ticket Resumen
    print("\n===============================================")
    print("         TICKET DE CONSUMO – PANCHITA           ")
    print("===============================================")
    print(f"{'Cant.':<6}{'Producto':<20}{'P.Unit':<10}{'Total':<10}")
    print("-----------------------------------------------")
    for prod in lista_productos:
        print(f"{prod['cantidad']:<6}{prod['nombre']:<20}S/.{prod['precio']:<7.2f}S/.{prod['subtotal_item']:<8.2f}")
    print("-----------------------------------------------")
    print(f"Subtotal Neto:                      S/. {subtotal_total:.2f}")
    print(f"Descuento Aplicado ({porcentaje_desc}%):          S/. {descuento_aplicado:.2f}")
    print(f"IGV (18%):                          S/. {igv:.2f}")
    print("-----------------------------------------------")
    print(f"TOTAL A PAGAR:                      S/. {total_final:.2f}")
    print("===============================================")
    # Resumen por persona
    print(f"Número de comensales:               {num_personas}")
    print(f"MONTO POR PERSONA:                  S/. {monto_por_persona:.2f}")
    print("===============================================\n")


# Ejecución del programa
if __name__ == "__main__":
    main()
    #Fin.