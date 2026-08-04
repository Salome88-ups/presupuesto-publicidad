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
def mejor_inversion(campanas, presupuesto):
    n = len(campanas)

    tabla = [[0] * (presupuesto + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        nombre, costo, retorno = campanas[i - 1]

        for p in range(presupuesto + 1):
            if costo > p:
                tabla[i][p] = tabla[i - 1][p]
            else:
                sin_campana = tabla[i - 1][p]
                con_campana = retorno + tabla[i - 1][p - costo]

                tabla[i][p] = max(
                    sin_campana,
                    con_campana
                )

    seleccionadas = []
    p = presupuesto

    for i in range(n, 0, -1):
        if tabla[i][p] != tabla[i - 1][p]:
            nombre, costo, retorno = campanas[i - 1]
            seleccionadas.append(nombre)
            p -= costo

    seleccionadas.reverse()

    return tabla[n][presupuesto], seleccionadas
if __name__ == "__main__":
    retorno_dp, seleccionadas_dp = mejor_inversion(
        campanas, presupuesto
    )

    retorno_greedy, seleccionadas_greedy = inversion_greedy(
        campanas, presupuesto
    )

    print("=== COMPARACIÓN DE MÉTODOS ===")

    print("\nProgramación Dinámica:")
    print("Campañas elegidas:", seleccionadas_dp)
    print("Retorno máximo:", retorno_dp, "mil dólares")

    print("\nGreedy:")
    print("Campañas elegidas:", seleccionadas_greedy)
    print("Retorno obtenido:", retorno_greedy, "mil dólares")

    print("\nDiferencia:")
    print(
        "La Programación Dinámica obtiene",
        retorno_dp - retorno_greedy,
        "mil dólares más de retorno."
    )