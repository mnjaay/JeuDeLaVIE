import numpy as np
import matplotlib.pyplot as screen
import matplotlib.animation as animation


#le nombre de colonne et de ligne 
rows = 100
cols = 100
# Initialisation de la varaible cell avec des cellules aléatoires vivantes=1 ou mortes=0
cell = np.random.choice([0, 1], size=(rows, cols))

# Fonction pour mettre à jour l'état de la cellule à chaque génération
def update(frameNum, image, cell, rows, cols):
    newCell = cell.copy()
    print(cell)  #verification de la cell avec les cellules aleatoire
    
    # Calcul du nombre de voisins vivants
    for rows,cols in np.ndindex(cell.shape):
            nbrCell = np.sum(cell[rows-1:rows+2,cols-1:cols+2]) - cell[rows,cols]
          
            # Appliquer les règles 
            if cell[rows,cols] == 1:
                if (nbrCell < 2) or (nbrCell > 3):
                    newCell[rows,cols] = 0
            else:
                if nbrCell == 3:
                    newCell[rows,cols] = 1
    image.set_data(newCell)
    cell[:] = newCell[:]
    return image


# l'affichage du programme 
fig, axe = screen.subplots()
#vous pouvez enlever interpolation et cmap pour avoir une vue plu claire des cellules
image = axe.imshow(cell, interpolation='sinc', cmap='hot')
animations = animation.FuncAnimation(
    fig, 
    update, 
    fargs=(image, cell, rows, cols), 
    frames=100, 
    interval=200, 
    save_count=50
)

screen.show()
