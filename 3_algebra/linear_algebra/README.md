# 5_linear_algebra
branch of mathematics that studies vectors and matrices¹
    studies the relationship between columns and rows.

def matrix:³
    square or rectangle of numbers.
    with special features.

def vector:
    physics
        an arrow with a:
            direction
            length
    mathematics
        anything with a sensible notion of:
            addition of two vectors
            multiplication of a vector by a number(scalar)

    computer science:
        list of numbers
        e.g | 1 |
            | 4 |

            || = []


Main Ideas(Types of matrices)² 
    Solving equations and systems of equations
        - A = CR : Independent columns  |   |
                                        |   | * |       |
                                        |   |
            a matrix A is a product of a Column matrix(C) and row matrix(R)
        
        - A = LU : Triangular matrices L and U  |\ o |        |\   |
                                                | \  |    *   | \  |
                                                |  \ |        |  \ |
                                                |   \|        | o \|
        
        - A = QR: Orthogonal columns in Q       |    |        |\   |
                                                |q₁qₙ|    *   | \  |
                                                |    |        |  \ |
                                                |    |        | o \|
                            

    Eigen values and singular values
        -
        -

References:
    https://www.3blue1brown.com/lessons/vectors
    2 Gilbert Strang.A 2020 Vision of Linear Algebra.
        https://ocw.mit.edu/courses/res-18-010-a-2020-vision-of-linear-algebra-spring-2020/resources/a-new-way-to-start-linear-algebra/
    1,3,4 Gilbert Strang.Part 1: The Column Space of a Matrix.https://ocw.mit.edu/courses/res-18-010-a-2020-vision-of-linear-algebra-spring-2020/resources/the-column-space-of-a-matrix/