class LoadingBar:
    def __init__(self, Name, Size, Goal, Level):
        self.name = Name
        self.size = Size
        self.goal = Goal
        if len(Name) > Level:
            print("Name too long for leveling. Continue with other value")
            self.level = len(Name)
        else:
            self.level = Level-len(Name)

    def draw(self, state):
        print(f"{self.name}: "+" "*self.level+"|"+"█"*int(state/self.goal*self.size)+" "*(self.size-int(state/self.goal*self.size))+"|"+f"    {int(state/self.goal*100)}%", end="\r")
    
    def finish(self):
        print(f"{self.name}: "+" "*self.level+"|"+"█"*self.size+"|"+f"    Done!")