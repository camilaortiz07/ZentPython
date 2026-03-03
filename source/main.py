gastos = {
    "comida": [],
    "transporte": [],
    "entretenimiento": [],
    "otros": []
}

def agregar_gasto():
    categoria = input("¿En qué categoría? ").lower()
    
    if categoria in gastos:           # ← Verifica que la categoría exista
        monto = float(input("¿Cuánto gastaste? $"))
        descripcion = input("Descripción breve: ")
        
        gastos[categoria].append({    # ← Agrega a la lista de esa categoría
            "monto": monto,
            "descripcion": descripcion
        })
    else:
        print("❌ Categoría no válida")
