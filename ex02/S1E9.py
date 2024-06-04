from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""
    @abstractmethod
    def __init__(self, first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Character",
                 eyes: str = "white",
                 hair: str = "white"):
        """Character constructor"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hair = hair

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass

    @abstractmethod
    def is_alive(self):
        """Check if the character is alive"""
        pass


    @abstractmethod
    def get_family_name(self):
        """Get the family name"""
        pass
    

    @abstractmethod
    def get_eyes(self):
        """Get the eyes color"""
        pass


    @abstractmethod
    def get_hair(self):
        """Get the hair color"""
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
