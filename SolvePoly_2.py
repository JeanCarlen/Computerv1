import re

def analyser_equation(equation):
    """Analyse l'équation et extrait les coefficients a, b, c."""
    equation = equation.replace(" ", "")  # Supprimer les espaces
    match = re.match(r"([-+]?\d*\.?\d*)x\^2([-+]?\d*\.?\d*)x([-+]?\d*\.?\d*)=0", equation)
    if not match:
        raise ValueError("Format d'équation invalide.")
    a, b, c = match.groups()
    a = float(a) if a else 1.0
    b = float(b) if b else 1.0
    c = float(c) if c else 0.0
    return a, b, c

def afficher_forme_reduite(a, b, c):
    """Affiche l'équation sous forme réduite."""
    signe_b = "+" if b >= 0 else "-"
    signe_c = "+" if c >= 0 else "-"
    print(f"{a}x^2 {signe_b} {abs(b)}x {signe_c} {abs(c)} = 0")

def calculer_degre(a, b):
    """Détermine le degré de l'équation."""
    if a != 0:
        return 2
    elif b != 0:
        return 1
    else:
        return 0

def calculer_discriminant(a, b, c):
    """Calcule le discriminant."""
    return b**2 - 4*a*c

def racine_carree(nombre, precision=0.0001):
    """Implémente la racine carrée (méthode de Héron)."""
    if nombre < 0:
        return None  # Pas de racine réelle pour les nombres négatifs
    x = nombre / 2.0
    while True:
        x_nouveau = (x + nombre / x) / 2.0
        if abs(x - x_nouveau) < precision:
            return x_nouveau
        x = x_nouveau

def resoudre_equation(a, b, c, discriminant, degre):
    """Résout l'équation en fonction du degré et du discriminant."""
    if degre == 2:
        if discriminant > 0:
            x1 = (-b + racine_carree(discriminant)) / (2*a)
            x2 = (-b - racine_carree(discriminant)) / (2*a)
            print(f"Deux solutions réelles : x1 = {x1}, x2 = {x2}")
        elif discriminant == 0:
            x = -b / (2*a)
            print(f"Une solution réelle : x = {x}")
        else:
            print("Pas de solutions réelles.")
    elif degre == 1:
        x = -c / b
        print(f"Une solution réelle : x = {x}")
    else:
        if c == 0:
            print("L'équation est toujours vraie.")
        else:
            print("L'équation est toujours fausse.")

# Exemple d'utilisation
equation = "2x^2 -3x + 1=0"
try:
    a, b, c = analyser_equation(equation)
    afficher_forme_reduite(a, b, c)
    degre = calculer_degre(a, b)
    discriminant = calculer_discriminant(a, b, c)
    print(f"Discriminant : {discriminant}")
    resoudre_equation(a, b, c, discriminant, degre)
except ValueError as e:
    print(f"Erreur : {e}")

equation = "0x^2 + 4x - 8 = 0"
try:
    a, b, c = analyser_equation(equation)
    afficher_forme_reduite(a, b, c)
    degre = calculer_degre(a, b)
    discriminant = calculer_discriminant(a, b, c)
    print(f"Discriminant : {discriminant}")
    resoudre_equation(a, b, c, discriminant, degre)
except ValueError as e:
    print(f"Erreur : {e}")

equation = "0x^2 + 0x + 0 = 0"
try:
    a, b, c = analyser_equation(equation)
    afficher_forme_reduite(a, b, c)
    degre = calculer_degre(a, b)
    discriminant = calculer_discriminant(a, b, c)
    print(f"Discriminant : {discriminant}")
    resoudre_equation(a, b, c, discriminant, degre)
except ValueError as e:
    print(f"Erreur : {e}")

equation = "0x^2 + 0x + 5 = 0"
try:
    a, b, c = analyser_equation(equation)
    afficher_forme_reduite(a, b, c)
    degre = calculer_degre(a, b)
    discriminant = calculer_discriminant(a, b, c)
    print(f"Discriminant : {discriminant}")
    resoudre_equation(a, b, c, discriminant, degre)
except ValueError as e:
    print(f"Erreur : {e}")

equation = "x^2 - 1 = 0"
try:
    a, b, c = analyser_equation(equation)
    afficher_forme_reduite(a, b, c)
    degre = calculer_degre(a, b)
    discriminant = calculer_discriminant(a, b, c)
    print(f"Discriminant : {discriminant}")
    resoudre_equation(a, b, c, discriminant, degre)
except ValueError as e:
    print(f"Erreur : {e}")