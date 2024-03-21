from time import sleep

class EricSpeed:
    def __init__(self, opponent):
        self.speed = 100
        self.health = 100
    
    def run(self):
        print("Nnnnnyuuum.....x5")
        

class Ivan:
    def __init__(self):
        self.dark_hound_magic = 95
        self.health = 100
        self.opponent_health = 100
        self.intellect = 80

    def magic_attack(self):
        print('boom')
        self.dark_hound_magic = self.dark_hound_magic - 1
        self.opponent_health = self.opponent_health - 5
        print('your magic health is: ', self.dark_hound_magic)

    def run(self):
        def refill():
            sprint = 5
            return sprint
             
        sprint = 5
        for _ in (0,sprint):
            print('running',end=" ")
            sprint -= sprint
            if sprint<0:
                print("sorry can't run!")
            
        if sprint==0:
            print("")
            inp = input("Do you want to refill? (Y/n):")
            if inp == "Y":
                print("wait for 5 seconds for refil")
                sleep(3)
                print("done, sprint ability restored ", refill())
            elif inp =="N" or "n":
                print("exiting")
                return
            else:
                print("invalid exiting")
                return
            



class EpicIvan(Ivan):
    def __inti__(self):
        self.health = 150          
    def EpicPunch(self):
        self.opponent_health = self.opponent_health - 10
        print("Opponent health has been compromised to with the epic punch: ", self.opponent_health)
    
    
epic_ivan = EpicIvan()    
epic_ivan.run()

epic_ivan.EpicPunch()

print("\n\tIvan fights\n")
ivan = Ivan()
ivan.run()
ivan.magic_attack()

eric = EricSpeed(ivan)
eric.run()

print("\nlets see whats the type of ivan, epic ivan and eric")
for chars in [ivan, epic_ivan, eric]:
    print(type(chars))

        
