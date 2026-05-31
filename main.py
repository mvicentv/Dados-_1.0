
import time
import dice


def roll_dice(amount: int, sides: int) -> list:
    """
    Devuelve una lista de tamaño 'amount' con los resultados
    de lanzar un dado de 'sides' caras.
    """
    results = dice.roll(f"{amount}d{sides}")
    return list(results)


def main():
    amount = 6
    sides = 20
    

    results = roll_dice(amount, sides)

    for i, result in enumerate(results, start=1):
        print(f"Lanzamiento {i} número obtenido {result}")
        if i < len(results):
            time.sleep(5)


if __name__ == "__main__":
    main()
