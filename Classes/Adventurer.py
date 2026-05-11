class Adventurer:
    def __init__(self, Name, Gender, Age):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.Items = {}
        # inventory key, dictonary {
        # ItemName:string,
        # ItemAmount:number
        # ExtraData:{ string : any}
        # }
        self.pos = [0, 0]

    def describe(self):
        print(f"Your name : {self.Name}")
        print(f"Your gender : {self.Gender}")
        print(f"Your age : {self.Age}")
        print(f"You are currently located at {self.pos[0]} x & {self.pos[1]} y")

    def update_pos(self, x, y):
        self.pos = [x, y]

    def change_pos(self, x, y):
        self.pos = [self.pos[0] + x, self.pos[1] + y]
