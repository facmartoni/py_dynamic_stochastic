import random


def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.randint(1, 6)
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros


def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    tiros_con_1_por_secuencia = []

    # for tiro in tiros:
    #     if 1 in tiro:
    #         tiros_con_1 += 1

    for secuencia in tiros:
        for tiro in secuencia:
            if tiro == 1:
                tiros_con_1 += 1
        tiros_con_1_por_secuencia.append(tiros_con_1)
        tiros_con_1 = 0

    probabilidades = []

    for tiros_con_1 in tiros_con_1_por_secuencia:
        probabilidad = tiros_con_1 / numero_de_tiros
        probabilidades.append(probabilidad)

    probabilidad_tiros_con_1 = sum(probabilidades) / numero_de_intentos

    print(
        f'Probabilidad de obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantos tiros del dado: '))
    numero_de_intentos = int(
        input('Cuantas veces quieres correr la simulación: '))
    main(numero_de_tiros, numero_de_intentos)
