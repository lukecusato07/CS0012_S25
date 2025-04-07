#### PROJECT 3 ####
#**************************************************#
#                                                  #
#  THIS FILE CONTAINS SOME OF THE CODE TO HELP     #
#     YOU TO GET GOING, BUT IT'S NOT FISHINED      #
#  AND WILL NOT RUN. YOU NEED TO MODIFY IT AND     #
#  AND ADD THE REMAINING CODE.                     #
#                                                  #
# NOTE THAT THE ATTRIBUTES DON'T NEED TO BE PRIVATE#
#**************************************************#
from random import randint

class Coin:
    def __init__(self, type):
        #type : 1 for penny, 5 for a nickel
        self.type = type
        self.content = True #by default, coin is content
    def getType(self):
        return self.type
    def getContent(self):
        return self.content
    def make_Content(self):
        self.content = not(self.content)
    def __str__(self):
        if self.content == True:
            return str(self.type) + 'C' #content
        return str(self.type) + 'D' #discontent

class Grid:
    def __init__(self):
        # 16 cols, 13 rows
        self.coins = [[None for i in range(16)] for i in range(13)] #redefining coins / declaration of list
        self.pennyCount = 1    #attribute count for pennies
        self.nickelCount = 1    #attribute count for nickels
        self.noneCount = 1
        for i in range(13):
            for j in range(16):
                self.randomized = False
                while self.randomized == False:
                    self.randomNum = randint(0,3)   #create random number
                    if self.randomNum == 0 and self.noneCount <= 58:
                        self.noneCount += 1
                        self.randomized = True
                    elif self.randomNum == 1 and self.pennyCount <= 75:
                        self.coins[i][j] = Coin(1)      # Place a penny
                        self.pennyCount += 1
                        self.randomized = True
                    elif self.randomNum == 2 and self.nickelCount <= 75:
                        self.coins[i][j] = Coin(5)      # Place a nickle
                        self.nickelCount += 1
                        self.randomized = True

        # add your code here

    # Part 2
    def check_content(self):
        for i in range(13):         # Loop through rows
            for j in range(16):     # Loop through cols
                current_coin = self.coins[i][j]     # Curr coordinate
                if current_coin == None:
                    continue
                
                # Initialize possible neighbors
                nw = None
                n = None
                ne = None
                w = None
                e = None
                sw = None
                s = None
                se = None
                
                # Based on coin's position, we access the different neighbors accordingly
                if i > 0 and j > 0:
                    nw = self.coins[i - 1][j - 1]
                if i > 0:
                    n = self.coins[i - 1][j]
                if i > 0 and j < 15:
                    ne = self.coins[i - 1][j + 1]
                if j > 0:
                    w = self.coins[i][j - 1]
                if j < 15:
                    e = self.coins[i][j + 1]
                if i < 12 and j > 0:
                    sw = self.coins[i + 1][j - 1]
                if i < 12:
                    s = self.coins[i + 1][j]
                if i < 12 and j < 15:
                    se = self.coins[i + 1][j + 1]

                # Want to check the amount of neighbors so we know how many for content
                neighbor_count = 0
                neighbor_same_count = 0

                # Checking the neighbor's type against the current type
                if nw:
                    neighbor_count += 1
                    if nw.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if n:
                    neighbor_count += 1
                    if n.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if ne:
                    neighbor_count += 1
                    if ne.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if w:
                    neighbor_count += 1
                    if w.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if e:
                    neighbor_count += 1
                    if e.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if sw:
                    neighbor_count += 1
                    if sw.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if s:
                    neighbor_count += 1
                    if s.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if se:
                    neighbor_count += 1
                    if se.getType() == current_coin.getType():
                        neighbor_same_count += 1
                if neighbor_count == 0:
                    continue
                
                # Happiness == >= half of the neighbors are of the same type
                happiness = neighbor_same_count / neighbor_count
                if current_coin.getContent() == True and happiness < 0.5:
                    current_coin.make_Content()     # Make the couin discontent if not half neighbors the same

    def move_discontent(self):
        # add your code here
        pass  #used as place holder while there's no code in the method
              #you can remove 'pass' once you have implemented the code.

    def __str__(self):
        output = ""
        for i in range(13):
            for j in range(16):
                if type(self.coins[i][j]) == Coin:
                        output+=str(self.coins[i][j])+' '
                else:
                    output+="__ "
            output+="\n"
        return output


def main():
    # part 1 of project 3
    # create a grid object
    grid = Grid()
    grid.check_content()
    # print out that grid object
    print(grid)
    pass  #used as place holder while there's no code in the method
              #you can remove 'pass' once you have implemented the code.

if __name__ == '__main__':
    main()
