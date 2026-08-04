campanas = [
    ("video en redes", 6, 30),
    ("email marketing", 5, 20),
    ("feria local", 5, 20),
]

presupuesto = 10


def inversion_greedy(campanas, presupuesto):
    ordenadas = sorted(
        campanas,
        key=lambda campana: campana[2] / campana[1],
        reverse=True
    )

    seleccionadas = []
    retorno_total = 0
    presupuesto_restante = presupuesto

    for nombre, costo, retorno in ordenadas:
        if costo <= presupuesto_restante:
            seleccionadas.append(nombre)
            retorno_total += retorno
            presupuesto_restante -= costo

    return retorno_total, seleccionadas