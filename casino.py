import random


class Casino:
    def __init__(self, name, color, sum):
        self.name = name
        self.color = color
        self.sum = sum

    def play(self):
        winc = random.randint(0, 36)
        if winc == 0:
            x = 'green'
            print('green')
        elif winc % 2 == 0:
            x = 'black'
            print('black')
        elif winc % 2 > 0:
            x = 'red'
            print('red')
        if x == self.color and not 'green':
            print(f'{self.name} ,you won {self.sum * 2}')
            with open('results.txt', 'a') as f:
                f.write(f"'{self.name}' bet '{self.color}' and won - {self.sum * 2}\n")
        elif x == self.color and 'green':
            print(f'{self.name}, you won {self.sum * 10}')
            with open('results.txt', 'a') as f:
                f.write(f"'{self.name}' bet '{self.color}' and won - {self.sum * 10}")
        else:
            print(f"{self.name}, you've lost {self.sum}")
            with open('results.txt', 'a') as f:
                f.write(f"'{self.name}' bet '{self.color}' and lost - {self.sum * 2}\n")

    def reset():
        with open('results.txt', 'w') as f:
            f.close()


Bet = Casino('ablai', 'black', 150)
Casino.play(Bet)
Casino.reset()
