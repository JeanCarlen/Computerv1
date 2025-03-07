import re


def analyser_equation(equation):
    equation = equation.replace(" ", "")
    parts = equation.split("=")
    # print("\n equation is ", equation, " and parts are ", parts)
    if len(parts) != 2:
        return ValueError("Format d'équation invalide.")
    left = parts[0]
    right = parts[1]

    def parse_term(term):
        match = re.match(r"([-+]?\d*\.?\d*)\*X\^(\d+)", term)  # find the coefficient and power of X
        if not match:
            return ValueError(f"Terme invalide: {term}")
        coeff, power = match.groups()
        return float(coeff), int(power)

    left_terms = [parse_term(t) for t in re.findall(r"[-+]?\d*\.?\d*\*X\^\d+", left)]
    right_terms = [parse_term(t) for t in re.findall(r"[-+]?\d*\.?\d*\*X\^\d+", right)]

    coeffs = {}
    for coeff, power in left_terms:
        if coeff != 0:
            coeffs[power] = coeffs.get(power, 0) + coeff
    # print("\n the dico left is ", coeffs)
    for coeff, power in right_terms:
        if coeff != 0:
            coeffs[power] = coeffs.get(power, 0) - coeff
    #     print("\n in the right for", coeffs[power])
    # print("\n the dico is ", coeffs)
    return coeffs


def reduce_form(coeffs):
    terms = []
    for power in sorted(coeffs.keys(), reverse=True):
        coeff = coeffs[power]
        if coeff != 0:
            sign = ""
            if coeff > 0 and terms:
                sign = "+"
            terms.append(f"{sign}{coeff} * X^{power}")
    if not terms:
        print("Reduced form: 0 = 0")
    else:
        print("Reduced form: " + " ".join(terms) + " = 0")


def find_degree(coeffs):
    if not coeffs:
        return 0
    return max(coeffs.keys())  # return the highest power of X


def find_discriminant(coeffs):
    """Calcule le discriminant."""  # b^2 - 4ac equation 2nd degree
    a = coeffs.get(2, 0)
    b = coeffs.get(1, 0)
    c = coeffs.get(0, 0)
    return b**2 - 4*a*c


def racine_carree(nombre, precision=0.0001):
    if nombre < 0:
        return None
    x = nombre / 2.0
    while True:
        x_new = (x + nombre / x) / 2.0
        if abs(x - x_new) < precision:
            return x_new
        x = x_new


def solve_equation(coeffs, discriminant, degre):
    if degre > 2:
        print("The polynomial degree is stricly greater than 2")
        return

    if degre == 2:
        if discriminant > 0:
            a = coeffs.get(2, 0)
            b = coeffs.get(1, 0)
            x1 = (-b + racine_carree(discriminant)) / (2*a)
            x2 = (-b - racine_carree(discriminant)) / (2*a)
            print("Discriminant is strictly positive, the two solutions are:")
            # rounding x1 and x2 to 8 decimal places
            x1 = round(x1, 8)
            x2 = round(x2, 8)
            print(x1)
            print(x2)
            return ([x1, x2])
        elif discriminant == 0:
            a = coeffs.get(2, 0)
            b = coeffs.get(1, 0)
            x = -b / (2*a)
            print("The solution is:")
            # rounding x to 8 decimal places
            x = round(x, 8)
            print(x)
            return ([x])
        else:
            print("Discriminant is strictly negative, there is no solution in R:")
    elif degre == 1:
        b = coeffs.get(1, 0)
        c = coeffs.get(0, 0)
        x = -c / b
        print("The solution is:")
        # rounding x to 8 decimal places
        x = round(x, 8)
        print(x)
        return ([x])
    elif degre == 0:
        c = coeffs.get(0, 0)
        if c == 0:
            print("All real numbers are solutions.")
        else:
            print("There is no solution.")


def main(equation):
    coeffs = analyser_equation(equation)
    reduce_form(coeffs)
    degre = find_degree(coeffs)
    print(f"Polynomial degree: {degre}")
    if degre <= 2:
        discriminant = find_discriminant(coeffs)
        return solve_equation(coeffs, discriminant, degre)
    else:
        return solve_equation(coeffs, 0, degre)
