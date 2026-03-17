class Point:
    def __init__(self,x,y):
        self.abscisse=x
        self.ordonnee=y

class RectanglePlus:
    def __init__(self,lg,la,pt):
        self.longueur=lg
        self.largeur=la
        self.Point_depart=pt

    def Perimetre(self):
        return 2*(self.longueur + self.largeur)
    
    def Air(self):
        return self.longueur * self.largeur
    
    def Dessine(self):
        F=pylab.gcal()
        rec = pylab.rectangle( (self.Point_depart.abscisse , self.Point_depart.ordonnee ) , self.longueur, self.largeur, fill=False  )
        F.add_patch(rec)
        pylab.axis([-50, 50, -50, 50])
        pylab.show()
        
    
        