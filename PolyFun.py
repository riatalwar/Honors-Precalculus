## Ria Talwar, Honors Precalculus, February 1, 2022
## Assignment 2: Polynomial Derivatives
## Find the derivative of a polynomial

## Import Modules
import numpy as np
import matplotlib.pyplot as plt

## FUNCTIONS

def poly_to_str(coeffs):
    '''
    Description: Creates a string representation of the polynomial equation
    Parameters: Array coeffecients
    Return: String equation
    '''
    equation = ''
    for i in range(len(coeffs)):
        if coeffs[i] != 0:  # Skip if coefficient is 0
            if i == 0:      # No x or () if coef for x^0
                string = str(coeffs[i])
            else:
                string = '(' + str(coeffs[i]) + ')x^' + str(i)

            if len(equation) != 0:    # No plus if length of equation == 0
                equation = string + ' + ' + equation
            else:
                equation = string
    return equation

def poly_eval(coeffs, inputs):
    '''
    Description: Calculates the outputs of the polynomial.
    Parameters: Array coefficients, Array inputs
    Return: Array outputs
    '''
    outputs = coeffs[0] * inputs ** 0   # Coef for x^0
    for i in range(1, len(coeffs)):     # Iterate over remaining coeffecients
        outputs = outputs + coeffs[i] * inputs ** i
    return outputs

def poly_diff(coeffs):
    '''
    Description: Find the derivative of a polynomial
    Parameters: Array coeffiecients of polynomial
    Return: Array coefficients of derivative
    '''
    deriv = coeffs * np.arange(len(coeffs))
    deriv = np.delete(deriv, 0)
    return deriv

def poly_multiply(coeffs1, coeffs2):
    '''
    Description: Multiply two polynomials together
    Parameters: Array coeffecients of p1, Array coeffecients of p2
    Return: Array new coefficients
    '''
    newCoeffs = [0] * (len(coeffs1) + len(coeffs2) - 1)     # Determine number of new coefficients
    for i in range(len(coeffs1)):
        for j in range(len(coeffs2)):
            x = i + j                                       # Get degree of current coeff
            newCoeffs[x] += coeffs1[i] * coeffs2[j]         # Add new value to current coeff at index
    return np.array(newCoeffs)                              # Convert to np array and return

def get_coeffs():
    '''
    Description: Get the coefficients of a polynomial from user
    Parameters: Void
    Return: Array coefficients
    '''
    coeffs = []
    i = 0
    while True:     # Loop forever unless break activated within loop
        inp = input('Enter the coefficient for x^' + str(i) + ' or hit ENTER to stop: ')
        try:    # See if user entered valid number and add to array
            inp = float(inp)
            coeffs.append(inp)
        except:
            if inp == '':   # Break if user hits enter
                break
            else:           # Take care of other non-numerical input
                continue
        i += 1
    return np.array(coeffs)


def test_poly_to_str():
    print(poly_to_str(np.array([1, -2, 3])) == '(3)x^2 + (-2)x^1 + 1')
    print(poly_to_str(np.array([1])) == '1')
    print(poly_to_str(np.array([1, 2, 3, 4])) == '(4)x^3 + (3)x^2 + (2)x^1 + 1')
    print(poly_to_str(np.array([1, 2])) == '(2)x^1 + 1')
    print(poly_to_str(np.array([1, -2, 3, -4, 5])) == '(5)x^4 + (-4)x^3 + (3)x^2 + (-2)x^1 + 1')
    print(poly_to_str(np.array([1, -2, 0, -4, 0])) == '(-4)x^3 + (-2)x^1 + 1')
    print(poly_to_str(np.array([0])) == '')
    print(poly_to_str(np.array([1, -2, 0, 0, 5])) == '(5)x^4 + (-2)x^1 + 1')
    print(poly_to_str(np.array([0, 0, 5])) == '(5)x^2')

def test_poly_eval():
    print(poly_eval(np.array([0]), np.array([1, 2, 3])) == np.array([0, 0, 0]))
    print(poly_eval(np.array([0, 1]), np.array([1, 2, 3])) == np.array([1, 2, 3]))
    print(poly_eval(np.array([1, 2]), np.array([1, 2, 3])) == np.array([3, 5, 7]))
    print(poly_eval(np.array([3, 2, 1]), np.array([1, 2, 3])) == np.array([6, 11, 18]))

def test_poly_diff():
    print(poly_diff(np.array([0])) == np.array([]))
    print(poly_diff(np.array([0, 1])) == np.array([1]))
    print(poly_diff(np.array([1, 2])) == np.array([2]))
    print(poly_diff(np.array([3, 2, 1])) == np.array([2, 2]))
    print(poly_diff(np.array([3, 2, 1, -3])) == np.array([2, 2, -9]))

def test_poly_multiply():
    print(poly_multiply(np.array([0]), np.array([0])) == np.array([0]))
    print(poly_multiply(np.array([0, 1]), np.array([0])) == np.array([0, 0]))
    print(poly_multiply(np.array([1, 2]), np.array([1])) == np.array([1, 2]))
    print(poly_multiply(np.array([3, 2, 1]), np.array([1])) == np.array([3, 2, 1]))
    print(poly_multiply(np.array([1, 2]), np.array([3, 4])) == np.array([3, 10, 8]))
    print(poly_multiply(np.array([1, 2]), np.array([-3, 4])) == np.array([-3, -2, 8]))

def test():
    print('poly_to_str')
    test_poly_to_str()
    print('\npoly_eval')
    test_poly_eval()
    print('\npoly_diff')
    test_poly_diff()


def run_derivative():
    ## INPUTS
    coeffs = get_coeffs()

    # Parameters for plotting
    xMin = -10
    xMax = 10
    numPts = 200

    ## CALCULATIONS
    # Create a string to display the equation of the polynomial
    eqn = poly_to_str(coeffs)

    # Generate the points on the curve over the domain xMin to xMax for polynomial and derivative
    x = np.linspace(xMin, xMax, numPts)
    y = poly_eval(coeffs, x)

    deriv = poly_diff(coeffs)
    yd = poly_eval(deriv, x)
    dequ = poly_to_str(deriv)

    ## OUTPUT
    print(eqn)  # Print the equation to the console
    print(dequ) # Print the derivative to the console

    plt.plot(x, y)  # Plot the polynomial
    plt.plot(x, yd) # Plot the derivative
    plt.grid(True)
    plt.show()

def run_multiply():
    ## INPUTS
    print('Enter coefficients for polynomial 1:')
    coeffs1 = get_coeffs()

    print('\nEnter coefficients for polynomial 2:')
    coeffs2 = get_coeffs()

    xMin = -10
    xMax = 10
    numPts = 200

    ## CALCULATIONS
    newCoeffs = poly_multiply(coeffs1, coeffs2)

    x = np.linspace(xMin, xMax, numPts)

    y1 = poly_eval(coeffs1, x)      # Get ycoords for polynomial 1
    y2 = poly_eval(coeffs2, x)      # Get ycoords for polynomial 2
    ynew = poly_eval(newCoeffs, x)  # Get ycoords for product

    ## OUTPUTS
    print('\n(' + poly_to_str(coeffs1) + ') * (' + poly_to_str(coeffs2) + ')')
    print('= ' + poly_to_str(newCoeffs))

    plt.plot(x, y1)     # Plot polynomial 1
    plt.plot(x, y2)     # Plot polynomial 2
    plt.plot(x, ynew)   # Plot the product
    plt.grid(True)
    plt.show()

def run():
    print('MENU:')      # Provide options for user
    print('1. Get the derivative of a polynomial')
    print('2. Multiply two polynomials\n')

    # Get user choice
    inp = ''
    while True:
        inp = input('Pick an option by entering the corresponding number: ')
        if inp in ['1', '2']:
            break
        else:
            print('Invalid input.')
    print()

    # Run whatever user selected
    if inp == '1':
        run_derivative()
    else:
        run_multiply()

run()
