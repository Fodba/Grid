def getVoisins(matrice,i,j):
    voisins = []
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    
    for di,dj in directions:
        ni,nj = i + di, j + dj
        if 0 <= ni < len(matrice) and 0 <= nj < len(matrice[0]):
            voisins.append(matrice[ni][nj])
            
    return voisins

