from room import Room

class Building:

    def __init__(self, name: str, address: str, floors: int):
        self.name = name
        self.address: address = address
        self.floors: int = floors
        self.rooms: list[Room]

    def get_name(self) -> str:
        return self.name
    
    def get_address(self) -> str:
        return self.address
    
    def get_floors(self) -> str:
        return self.floors