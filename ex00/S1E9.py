from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass

    @abstractmethod
    def is_alive(self):
        """Check if the character is alive"""
        pass


class Stark(Character):
    """Stark class"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Stark constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Kill the Stark character"""
        self.is_alive = False

    def is_alive(self):
        """Check if the Stark character is alive"""
        return self.is_alive


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
