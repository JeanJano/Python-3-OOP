from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self,
                 first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Baratheon",
                 eyes: str = "brown",
                 hair: str = "dark"):
        """Baratheon constructor"""
        super().__init__(first_name, is_alive, family_name, eyes, hair)

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

    def get_hair(self):
        """Get the hair color"""
        return self.hair

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


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self,
                 first_name: str,
                 is_alive: bool = True,
                 family_name: str = "Lannister",
                 eyes: str = "blue",
                 hair: str = "light"):
        """Lannister constructor"""
        super().__init__(first_name, is_alive, family_name, eyes, hair)

    def die(self):
        """Kill the Lannister character"""
        self.is_alive = False

    def is_alive(self):
        """Check if the Lannister character is alive"""
        return self.is_alive

    def get_family_name(self):
        """Get the family name"""
        return self.family_name

    def get_eyes(self):
        """Get the eyes color"""
        return self.eyes

    def get_hair(self):
        """Get the hair color"""
        return self.hair

    @property
    def __repr__(self) -> str:
        __repr__ = f"""<bound method Lannister.__repr__ of Vector: ('
        {self.get_family_name()}', {self.get_eyes()}, {self.get_hair()})>"""
        return __repr__

    @property
    def __str__(self) -> str:
        __str__ = f"""<bound method Lannister.__str__ of Vector: ('
        {self.get_family_name()}', {self.get_eyes()}, {self.get_hair()})>"""
        return __str__

    def create_lannister(first_name: str, is_alive: bool = True):
        """Create a Lannister character"""
        return Lannister(first_name, is_alive)
