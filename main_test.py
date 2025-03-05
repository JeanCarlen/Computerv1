import math
import sys
import SolvePoly_2 as SP

#for testing
import random
import numpy as np


class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def main():
  if (len(sys.argv) < 2):
    print("WRONG FORMAT!")
    return
  if (sys.argv[1] == "R"):
    constant = [generate_random_polynomials(0) for _ in range(5)]
    linear = [generate_random_polynomials(1) for _ in range(5)]
    quadratic = [generate_random_polynomials(2) for _ in range(5)]
    above = [generate_random_polynomials(10) for _ in range(5)]
    equations = constant + linear + quadratic + above
  elif (sys.argv[1] == "T"):
    test_with_ans(sys)
    return
  else:
    equations = sys.argv[1:]

  for eq in equations:
    print("----------------")
    print("Equation: " + eq)
    SP.main(eq)
    print("----------------")


def test_with_ans(sys):
  total_tests = 100000
  success = 0
  fails = []
  if (len(sys.argv) == 3 and sys.argv[2].isdigit()):
    total_tests = int(sys.argv[2])
  quad = [generate_clean_polynomials(2) for _ in range(total_tests)]
  lin = [generate_clean_polynomials(1) for _ in range(total_tests)]
  all_poly = quad + lin
  for equ in all_poly:
    print('EQUATION: ', translate_clean(equ))
    ans_full = SP.main(translate_clean(equ))
    
    ans_t = [cust_round(ans_full[0])]
    if (len(ans_full) == 2):
      ans_t.append(cust_round(ans_full[1]))
    roots = np.roots(equ)
    #round roots from numpy
    rounded_roots = [cust_round(roots[0])]
    if (len(roots) == 2):
      rounded_roots.append(cust_round(roots[1]))
    if (ans_t == rounded_roots):
      print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
      success += 1
    else:
      if (type(ans_t) is list and len(ans_t) > 1):
        temp = ans_t[0]
        ans_t[0] = ans_t[1]
        ans_t[1] = temp
      if (ans_t == rounded_roots or ((type(ans_t) is float or type(ans_t) is int) and ans_t == rounded_roots[0])):
        print(bcolors.OKGREEN + "OK" + bcolors.ENDC)
        success += 1
      else:
        print(bcolors.FAIL + "KO" + bcolors.ENDC)
        print("Expected: " + str(rounded_roots))
        fails.append((ans_t, rounded_roots, roots))
  print(f"Result : {success}/{total_tests * 2}")
  if fails:
    print("\nFailed cases:")
    for ans_t, rounded_roots, roots in fails:
      print(f"Got: {ans_t}, Expected: {rounded_roots} BASE: {roots}")

def generate_random_polynomials(max_exp):

  a = round(random.uniform(-10, 10), 2)
  b = round(random.uniform(-10, 10), 2)
  c = round(random.uniform(-10, 10), 2)
  p = random.randint(0, max_exp)
  q = random.randint(0, max_exp)
  r = random.randint(0, max_exp)
  return f"{a} * X^{p} + {b} * X^{q} = {c} * X^{r}"


def generate_clean_polynomials(max_exp):
  a = round(random.uniform(-10, 10), 2)
  b = round(random.uniform(-10, 10), 2)
  c = round(random.uniform(-10, 10), 2)
  if (max_exp == 0):
    a = b = 0
  if (max_exp == 1):
    a = 0
  ans = [a, b, c]
  if (a == 0 and b == 0):
    ans = generate_clean_polynomials(max_exp)
  if ((b**2 - 4 * a * c) < 0):
    ans = generate_clean_polynomials(max_exp)
  return (ans)


def translate_clean(equ):
  a = equ[0]
  b = equ[1]
  c = equ[2]
  formatted = str(a) + " * X^2 + " + str(b) + " * X^1 + " + str(c) + " * X^0 = 0 * X^0"
  return (formatted)



def cust_round(number):
  ret = round(number, 6)
  if ret.is_integer():
    ret = int(ret)

  return ret

main()