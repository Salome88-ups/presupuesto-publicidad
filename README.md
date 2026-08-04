# presupuesto-publicidad
Proyecto de comparación entre Greedy y Programación Dinámica para inversión publicitaria.
# Presupuesto de Publicidad

## Greedy

La estrategia Greedy falla porque selecciona primero la campaña con mayor densidad de retorno por costo. En este caso, el video en redes tiene una densidad de 5.0 y genera un retorno de 30 mil dólares, pero ocupa 6 mil del presupuesto e impide contratar las dos campañas restantes. La Programación Dinámica demuestra que email marketing y feria local generan 40 mil dólares. La propiedad que no se cumple es la **elección localmente óptima**, ya que elegir la mejor densidad en cada paso no garantiza una solución global óptima.

## Divide y Vencerás

Este problema no se resuelve dividiendo las campañas en mitades independientes porque las decisiones de una parte afectan directamente al presupuesto disponible para la otra. Si se divide el conjunto de campañas, las soluciones parciales no pueden combinarse libremente sin considerar el límite total de 10 mil dólares. Por lo tanto, no se cumple la condición de que los subproblemas puedan resolverse de forma independiente y combinarse directamente para obtener la solución óptima.

## Programación Dinámica

En la tabla de Programación Dinámica, el estado representa el **máximo retorno posible utilizando las primeras i campañas con un presupuesto máximo p**. Los subproblemas se superponen porque diferentes combinaciones de campañas consultan repetidamente soluciones para los mismos presupuestos y subconjuntos de campañas. Cada casilla evalúa dos decisiones: no contratar la campaña actual o contratarla, siempre que exista presupuesto suficiente, y conserva la alternativa que produce el mayor retorno.

## Backtracking

Backtracking resolvería este problema explorando las decisiones de contratar o no contratar cada campaña, descartando las combinaciones que superen el presupuesto. Con 3 campañas existen **2³ = 8 subconjuntos posibles** para explorar. Con 30 campañas habría **2³⁰ = 1.073.741.824 subconjuntos**, lo que representa un crecimiento exponencial. Por esta razón, dejaría de ser viable rápidamente cuando el número de campañas aumente, especialmente si se requiere explorar prácticamente todas las combinaciones.
