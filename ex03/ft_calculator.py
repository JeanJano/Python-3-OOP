class calculator:

    def __init__(self, list) -> None:
        self.list = list


    def __add__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.list = [i + object for i in self.list]
            print(self.list)


    def __mul__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.list = [i * object for i in self.list]
            print(self.list)


    def __sub__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.list = [i - object for i in self.list]
            print(self.list)


    def __truediv__(self, object) -> None:
        if isinstance(object, (int, float)):
            self.list = [i / object for i in self.list]
            print(self.list)


# def main() -> None:
#     v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v1 + 5
#     print("---")
#     v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
#     v2 * 5
#     print("---")
#     v3 = calculator([10.0, 15.0, 20.0])
#     v3 - 5
#     v3 / 5

# if __name__ == "__main__":
#     main()
