import math
def delta(a,b,c):
    return b**2 -4*a*c
def NombreRacine( a,b,c):
    if(delta(a,b,c)<0):
        return 0
    elif(delta(a,b,c)==0):
        return 1
    else:
        return 2
def AfficheNombreRacine(a,b,c):
    print(NombreRacine(a,b,c))

def Racine1(a, b, c):
    if delta(a, b, c) >= 0:
        x1 = (-b + math.sqrt(delta(a, b, c))) / (2 * a)
        return x1
    else:
        return None

def Racine2(a, b, c):
    if delta(a, b, c) >= 0:
        x2 = (-b - math.sqrt(delta(a, b, c))) / (2 * a)
        return x2
    else:
        return None
def conversion_temps(h, m, s):
    return h * 3600 + m * 60 + s

def temps_ecoule(h1, m1, s1, h2, m2, s2):
    t1 = conversion_temps(h1, m1, s1)
    t2 = conversion_temps(h2, m2, s2)
    d = abs(t2 - t1)
    return d

def conversion_distance(km, m, cm):
    return km * 1000 + m + cm / 100

def vitesse(km, m, cm, h, ms, s):
    d_metres = conversion_distance(km, m, cm)
    temps_s = conversion_temps(h, ms, s)
    if temps_s == 0:
        return None
    else:
        v_mps = d_metres / temps_s
        return v_mps



