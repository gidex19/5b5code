import oop2

def zingle():
    print("zingle")


class Laptop:
    makeup = "steel"

    # ram = 0

    """ A class for creating laptop instances"""
    def __init__(self, brandname, color, ram):
        self.name = brandname
        self.color = color
        self.ram = ram

    def upgrade_ram(self, n):
        """a function to upgrade the RAM of a laptop"""
        print("upgrading RAM.....")
        # self.ram = self.ram * n
        self.ram += n

    @classmethod
    def update_cls_ram(cls, v):
        cls.ram += v

def home():
    print("hello")

print("hello oop1.py")
if __name__ == "__main__":
    print("we are within the oop1 file")
