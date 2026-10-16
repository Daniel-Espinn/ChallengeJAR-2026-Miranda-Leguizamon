# idea: Probar todas las funciones de relglas_cerebro.py
# aqui con pytest para evitar tener que launchear gazebo 
# cada vez que queremos probar funciones elementales.
# Evitamos que nos den errores tontos o resultados limites
# de tipo infinito culpa de dividir por cero o que
# queden reservas de segundo en negativo.
# Usamos pytest para testear rapido con tablas y probar todo lo que
# necesitamos en una iteracion de una viendo el resultado de cada una
# y si tiran los errores que deberian tirar o no

import pytest
