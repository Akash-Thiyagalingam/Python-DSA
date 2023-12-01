# Printing primid pattern using recursion
class pattern:
    def __init__ (self, n):
        self.n = n
        self.star = "*"
    def pyramid(self, space):
        if len(space) == self.n:
            return 
        self.pyramid(space + " " )
        print(space, end = "")
        print(self.star)
        self.star += " *"
        

pat=pattern(5)
pat.pyramid(" ")