class calculator:

    def __init__(self, list) -> None:
        """
        Initialize the class with a list of numbers.

        :param list: A list of numbers.
        """
        self.list = list

    def __add__(self, object) -> None:
        """
        Add a number to each element in the list.

        :param object: A number (int or float) to be added to each element
        in the list.
        """
        if isinstance(object, (int, float)):
            self.list = [i + object for i in self.list]
            print(self.list)

    def __mul__(self, object) -> None:
        """
        Multiply each element in the list by a number.

        :param object: A number (int or float) to multiply each element in
        the list by.
        """
        if isinstance(object, (int, float)):
            self.list = [i * object for i in self.list]
            print(self.list)

    def __sub__(self, object) -> None:
        """
        Subtract a number from each element in the list.

        :param object: A number (int or float) to be subtracted from each
        element in the list.
        """
        if isinstance(object, (int, float)):
            self.list = [i - object for i in self.list]
            print(self.list)

    def __truediv__(self, object) -> None:
        """
        Divide each element in the list by a number.

        :param object: A number (int or float) to divide each element in the
        list by.
        """
        assert object != 0, "Cannot divide by zero."
        if isinstance(object, (int, float)):
            self.list = [i / object for i in self.list]
            print(self.list)


def main() -> None:
    try:
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
        v3 / 0
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
