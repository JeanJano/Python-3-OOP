from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King from Baratheon and Lannister family"""
    def __init__(self,
                 first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Baratheon",
                 eyes: str = "brown",
                 hair: str = "dark"):
        """King constructor"""
        Baratheon.__init__(self, first_name, is_alive, family_name, eyes, hair)
        Lannister.__init__(self, first_name, is_alive, family_name, eyes, hair)

    def die(self):
        """Kill the Baratheon character"""
        self.is_alive = False

    def is_alive(self):
        """Check if the Baratheon character is alive"""
        return self.is_alive

    def get_family_name(self):
        """Get the family name"""
        return self.family_name

    def get_eyes(self):
        """Get the eyes color"""
        return self.eyes

    def get_hairs(self):
        """Get the hair color"""
        return self.hair

    def set_eyes(self, eyes: str):
        """Set the eyes color"""
        self.eyes = eyes

    def set_hairs(self, hair: str):
        """Set the hair color"""
        self.hair = hair

    @property
    def __repr__(self) -> str:
        __repr__ = f"""<bound method Baratheon.__repr__ of Vector: ('
        {self.get_family_name()}', {self.get_eyes()}, {self.get_hair()})>"""
        return __repr__

    @property
    def __str__(self) -> str:
        __str__ = f"""<bound method Baratheon.__str__ of Vector: ('
        {self.get_family_name()}', {self.get_eyes()}, {self.get_hair()})>"""
        return __str__


def main() -> None:
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
