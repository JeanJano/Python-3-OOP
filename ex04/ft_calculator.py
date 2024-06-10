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

    def dotproduct(a, b) -> None:
        """
        Calculate and print the dot product of two vectors.

        :param a: First vector, a list of numbers.
        :param b: Second vector, a list of numbers.
        """
        dot_product = 0
        for i in range(len(a)):
            dot_product += a[i] * b[i]
        print(f"Dot product is: {dot_product}")

    def add_vec(a, b) -> None:
        """
        Add two vectors and print the result.

        :param a: First vector, a list of numbers.
        :param b: Second vector, a list of numbers.
        """
        add_vec = []
        for i in range(len(a)):
            add_vec.append(float(a[i]) + float(b[i]))
        print(f"Add Vector is: {add_vec}")

    def sous_vec(a, b) -> None:
        """
        Subtract the second vector from the first and print the result.

        :param a: First vector, a list of numbers.
        :param b: Second vector, a list of numbers.
        """
        sous_vec = []
        for i in range(len(a)):
            sous_vec.append(float(a[i]) - float(b[i]))
        print(f"Sous Vector is: {sous_vec}")


def main() -> None:
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
