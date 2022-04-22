class MyZeroDiv(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


if __name__ == "__main__":
    from sys import exit

    a = 0
    b = 0
    try:
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
    except:
        print("Неверный ввод")
        exit(1)

    try:
        if b == 0:
            raise MyZeroDiv("При делении на 0 результат 0")
        print(f"Все в порядке {a}/{b} = {a / b}")
    except MyZeroDiv as ex:
        print(ex)
