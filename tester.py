from game import Game
from threading import Thread, Lock
import os

path_dest = "results.txt"

contador=0 

lck = Lock()

# Eliminar el archivo si existe
if os.path.exists(path_dest): os.remove(path_dest)


def play(game:Game):
    global contador
    
    if game.end():
        with lck:
            contador+=1
            if contador % 1000 == 0: print(contador)
            with open(path_dest, "a") as f:
                f.write(f"{game.log}\n{game}\n") 
        return
    else:
        for index in game.board.empty_cells():
            new_game = game.copy()
            new_game.play(*index)
            play(new_game)

    
    


gamex, gameo = Game("Player 1", "Player 2"), Game("Player 2", "Player 1")
gamedsl = gamex.copy()

firstx = Thread(target=play, args=(gamex,))
#firsto = Thread(target=play, args=(gameo,))
firstx.start()
#firsto.start()

firstx.join()
#firsto.join()


print(contador)