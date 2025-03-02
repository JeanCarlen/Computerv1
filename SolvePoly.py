import re

def parse_equation(equation):
    """Parses the equation and returns coefficients for X^0, X^1, X^2."""
    try:
        left, right = equation.split("=")
        left_terms = re.findall(r'([+-]?\d+(?:\.\d+)?)\s*\*\s*X\^(\d+)|([+-]?\d+(?:\.\d+)?)', left)
        right_terms = re.findall(r'([+-]?\d+(?:\.\d+)?)\s*\*\s*X\^(\d+)|([+-]?\d+(?:\.\d+)?)', right)

        coefficients = [0.0, 0.0, 0.0]  # Initialize with zeros, index 0: X^0, 1: X^1, 2: X^2

        for coef, power, const in left_terms:
            if coef:
                power = int(power) if power else 0
                if 0 <= power <= 2:
                    coefficients[power] += float(coef)
            elif const:
                coefficients[0] += float(const)

        for coef, power, const in right_terms:
            if coef:
                power = int(power) if power else 0
                if 0 <= power <= 2:
                    coefficients[power] -= float(coef)
            elif const:
                coefficients[0] -= float(const)

        return coefficients

    except ValueError as ve:
        raise ValueError("Equation format is incorrect: " + str(ve))
    except Exception as e:
        raise Exception("Error parsing equation: " + str(e))

def reduce_form(coefficients):
    """Creates the reduced form string."""
    terms = []
    for power, coef in reversed(list(enumerate(coefficients))):
        if coef != 0:
            if power == 0:
                terms.append(f"{coef:+.1f}")
            else:
                terms.append(f"{coef:+.1f} * X^{power}")

    if not terms:
        return "0 = 0"
    return " ".join(terms) + " = 0"

def solve_polynomial(coefficients):
    """Solves the polynomial based on its degree."""
    try:
        a, b, c = coefficients[2], coefficients[1], coefficients[0]

        if a != 0:  # Quadratic equation
            discriminant = b**2 - 4*a*c
            if discriminant > 0:
                sol1 = (-b + discriminant**0.5) / (2*a)
                sol2 = (-b - discriminant**0.5) / (2*a)
                return 2, discriminant, (sol1, sol2)
            elif discriminant == 0:
                sol = -b / (2*a)
                return 1, discriminant, (sol,)
            else:
                return 0, discriminant, None

        elif b != 0:  # Linear equation
            sol = -c / b
            return 1, None, (sol,)

        elif c == 0:  # Identity equation (0 = 0)
            return -1, None, None

        else:  # Contradiction equation (e.g., 5 = 0)
            return 0, None, None
    except Exception as e:
        raise Exception("Error solving polynomial: " + str(e))

def main(equation):
    try:
        coefficients = parse_equation(equation)
        reduced = reduce_form(coefficients)
        print("Reduced form:", reduced)

        non_zero_coeffs = [i for i, v in enumerate(coefficients) if v != 0]
        if not non_zero_coeffs:
            print("Reduced form: 0 = 0")
            print("Each real number is a solution.")
            return

        degree = max(non_zero_coeffs)
        print("Polynomial degree:", degree)

        if degree > 2:
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return

        num_solutions, discriminant, solutions = solve_polynomial(coefficients)

        if num_solutions == -1:
            print("Each real number is a solution.")
        elif num_solutions == 0:
            print("No solution.")
        elif degree == 2:
            if discriminant > 0:
                print("Discriminant is strictly positive, the two solutions are:")
            elif discriminant == 0:
                print("Discriminant is zero, the solution is:")
            else:
                print("Discriminant is strictly negative, no real solutions.")

            if solutions:
                for sol in solutions:
                    print(f"{sol:.6f}")
        elif degree == 1:
            print("The solution is:")
            print(f"{solutions[0]:.6f}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Linear:")
    print("first")
    main("5 * X^0 + 4 * X^1 = 0")
    print("second")
    main("2 * X^1 = 8")
    print("third")
    main("3 * X^1 - 5 * X^0 = 2 * X^0")
    print("\nQuadratic:")
    print("first")
    main("1 * X^2 - 5 * X^1 + 6 * X^0 = 0")
    print("second")
    main("1 * X^2 + 2 * X^1 + 1 * X^0 = 0")
    print("third")
    main("1 * X^2 + 1 * X^1 + 1 * X^0 = 0")
    print("\nEdge Cases:")
    print("first")
    main("0 * X^2 + 0 * X^1 + 0 * X^0 = 0")
    print("second")
    main("1 * X^0 = 0")
    print("\nHigher Degree:")
    main("1 * X^3 - 2 * X^2 + 3 * X^1 - 4 * X^0 = 0")
    print("\nSpecial Cases:")
    main("1 * X^0 = 1 * X^0")
    main("3 * X^0 = 5 * X^0")