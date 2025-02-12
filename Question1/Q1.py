# This is the .py file for Question 1 of Homework 3
# I will begin with part a of Q1

# Part a

import numpy as np
from scipy.integrate import nquad
from scipy.linalg import det, inv
from numpy.linalg import norm

def integrand(v, A, w):
    v = np.array(v)
    return np.exp(-0.5 * np.dot(v, np.dot(A, v)) + np.dot(v, w))

def closed_form(A, w):
    N = len(w)
    A_inv = inv(A)
    return (2 * np.pi) ** (N / 2) * (det(A_inv) ** 0.5) * np.exp(0.5 * np.dot(w, np.dot(A_inv, w)))

# Now that the two sides of the expression are defined, I will define a function that compares their outputs
def I(A, w):
    N = len(w)
    bounds = [(-np.inf, np.inf)] * N

    # This wrapper function was a critical addition that took over an hour of troubleshooting to figure out.
    # The dimensionality and the documentation of the nquad operation was very cryptic and kept returning
    # errors.
    
    def integrand_wrapper(*args):
        # *args here includes all v1, v2, ..., vN as separate arguments, we need to pack them into a list
        v = list(args) 
        return integrand(v, A, w)

    integral, _ = nquad(integrand_wrapper, bounds)
    
    closed_expr = closed_form(A, w)

    print(f"Integral: {integral}")
    print(f"Closed-form expression: {closed_expr}")
    
# I tested this function on the given A and w and got approximately the same numerical result.
# I will list the values and formalize the response in part b.

# Part b

# In reference to the matrices given:
A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
A_prime = np.array([[4, 2, 1], [2, 1, 3], [1, 3, 6]])
w = np.array([1, 2, 3])

print("Below is the result of the A matrix")
I(A, w)

print("Below is the result of the A' matrix")
I(A_prime, w)

# Ok so heres the deal.
# I will include a .png of a screenshot I took of my terminal but I have never seen anything like what popped up.
# The first value for I(A, w) was computed successfully so I know that the actual program is functional.
# The value for both equations for I(A, w) was about 4.2758. But as my computer transitioned to the A' matrix the system
# overloaded and I got many warnings as to the size of the computation. I even tried to compute the second matrix 
# independently in a different .py window but my computer still faltered. I will try to get a value from a peer so I can 
# compare with the original A matrix but otherwise I do not believe my computer can handle the calculation.

# Part c

import numpy as np
from scipy.linalg import inv, det
from numpy.linalg import inv

def calculate_moments(A, w):
    N = A.shape[0]
    A_inv = inv(A)
    mean = np.dot(A_inv, w)
    
    moments = {}
    # Below here is specifically for the first moments
    for i in range(N):
        moments[f'v{i+1}'] = mean[i]

    # And starting here is for the second moments
    for i in range(N):
        for j in range(i, N):
            if i == j:
                moments[f'v{i+1}^2'] = A_inv[i, j] + mean[i]**2
            else:
                moments[f'v{i+1}v{j+1}'] = A_inv[i, j] + mean[i] * mean[j]

    return moments

# Now employing the given matrices
A = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])
w = np.array([1, 2, 3])

moments = calculate_moments(A, w)
print("Calculated Moments:")
# iterating for every scenario
for moment, value in moments.items():
    print(f"{moment}: {value}")

# Terminal is taking too long to run the whole code so I had to run the part c results in a 
# separate .py file. The (approximate) results are below:

# v1: 0.08955223880597016
# v2: 0.10447761194029859
# v3: 0.4328358208955224
# v1^2: 0.32145243929605705
# v1v2: -0.12497215415460013
# v1v3: 0.0536867899309423
# v2^2: 0.3541991534862999
# v2v3: -0.1040320784139006
# v3^2: 0.4261528179995545
