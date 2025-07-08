# Importing Selenium Package 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By 

# Importing Stockfish 
from stockfish import Stockfish

# Chess Handeling Class 
class Chess:
    def __init__(self):
        self.driver = None
        self.stockfish = Stockfish("stockfish/stockfish-windows-x86-64-avx2.exe") # Path to Stockfish excecutable file
        self.position = [] # Stores list of position made in the current game
        # Conversion Disctionary 
        self.indi = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h'}
        self.alf_to_indi = {'a':'1', 'b': '2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8'}

    # Open the chess website
    def open_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.chess.com/')
        input("Enter:")

    # Retrive the recent move in online mode 
    def get_move_online(self):
        # Retrive the Positions of last chess piece 
        ini_pos = [self.driver.find_element(By.XPATH,'//*[@id="board-single"]/div[3]'), self.driver.find_element(By.XPATH,'//*[@id="board-single"]/div[2]')]
        pos = []
        for i in ini_pos:
            move = i.get_attribute('class')
            old = []
            for j in move:
                try:
                    old.append(int(j))
                except ValueError:
                    continue
            if len(old) < 1:
                continue
            old[0],old[1] = self.indi[old[0]],str(old[1])
            old = ''.join(old)
            pos.append(old)
        
        moves = self.driver.find_elements(By.CLASS_NAME, "main-line-row")
        if len(moves) < 1:
            return 
        if len(moves) > 0:
            move = (moves[-1].text).split('\n')
            idx = -3 if len(move) > 3 else -2
            if '+' in move[idx]:
                new = move[idx][-3:-1]
            elif 'O-O' in move[idx]:
                try:
                    if 'KING' in  self.stockfish.get_what_is_on_square(pos[0]).name:
                        new = pos[0] + pos[1]
                except AttributeError:
                    if 'KING' in  self.stockfish.get_what_is_on_square(pos[1]).name:
                        new = pos[1] + pos[0]
                self.position.append(new)
                return

            else:
                new = move[idx][-2:] 
            for i in pos:
                if i == new:
                    continue
                i += new
                self.position.append(i)
    
    # Retrive the recent move in offline mode 
    def get_move(self):
        # Initial positions of the chess piece 
        ini_pos = [self.driver.find_element(By.XPATH, '//*[@id="board-play-computer"]/div[2]'), self.driver.find_element(By.XPATH, '//*[@id="board-play-computer"]/div[3]')]
        pos = [] # Temp position 
        for i in ini_pos:
            move = i.get_attribute('class')
            old = []
            for j in move:
                try:
                    old.append(int(j))
                except ValueError:
                    continue
            if len(old) < 1:
                continue
            old[0],old[1] = self.indi[old[0]],str(old[1])
            old = ''.join(old)
            pos.append(old)
        
        moves = self.driver.find_elements(By.CLASS_NAME, "main-line-row")
        if len(moves) < 1:
            return 
        move = (moves[-1].text).split('\n')
        if '+' in move[-1]:
            new = move[-1][-3:-1]
        elif 'O-O' in move[-1]:
            try:
                if 'KING' in  self.stockfish.get_what_is_on_square(pos[0]).name:
                    new = pos[0] + pos[1]
            except AttributeError:
                if 'KING' in  self.stockfish.get_what_is_on_square(pos[1]).name:
                    new = pos[1] + pos[0]
            self.position.append(new)
            return

        else:
            new = move[-1][-2:] 
        for i in pos:
            if i == new:
                continue
            i += new
            self.position.append(i)
    

    # Automating the guessed move to make the move on it's own
    def automate(self):
        action = ActionChains(self.driver)
        recent_move = self.position[-1]
        recent_move = list(recent_move)
        for i in range(len(recent_move)):
            try:
                recent_move[i] = self.alf_to_indi[recent_move[i]]
            except KeyError:
                continue
        half = [''.join(recent_move[:2]),''.join(recent_move[2:])]

        tap1 = self.driver.find_elements(By.CLASS_NAME, f'square-{half[0]}')
        action.click(tap1[-1]).perform()
        tap2 = self.driver.find_elements(By.CLASS_NAME, f'square-{half[1]}')
        action.click(tap2[-1]).perform()

    # Guess the next move in online mode 
    def new_move(self):
        self.get_move()
        self.stockfish.set_position(self.position)
        move = self.stockfish.get_best_move()
        self.position.append(move)
        self.automate()

    # Guess the next move in offline mode 
    def new_move_online(self):
        self.get_move_online()
        self.stockfish.set_position(self.position)
        move = self.stockfish.get_best_move()
        self.position.append(move)
        self.automate()

    # Reset the position List to Null
    def reset(self):
        self.position = []
    
    # Run the offline attributes 
    def run_bot_offline(self):
        self.new_move()
                
    # Run the online attributes 
    def run_bot_online(self):
        
        self.new_move_online()
