# 5_linear_algebra
branch of mathematics that studies vectors and matrices
    studies the relationship between columns and rows (Strang, 2020).

def matrix:
    square or rectangle of numbers
    with special features (Strang, 2020).

def vector:
    physics
        an arrow with a:
            direction
            length (Sanderson, 2016).
    mathematics
        anything with a sensible notion of:
            addition of two vectors
            multiplication of a vector by a number(scalar) (Sanderson, 2016).

    computer science:
        list of numbers (Sanderson, 2016).
        e.g | 1 |
            | 4 |

            || = []


Main Ideas(Types of matrices)(Strang, 2010)
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

references:
    Sanderson G. 2016. Vectors, what even are they?. https://www.3blue1brown.com/lessons/vectors
    Strang, G. 2010. A 2020 Vision of Linear Algebra. https://ocw.mit.edu/courses/res-18-010-a-2020-vision-of-linear-algebra-spring-2020/resources/a-new-way-to-start-linear-algebra/.
    Strang, G. 2020. Part 1: The Column Space of a Matrix. https://ocw.mit.edu/courses/res-18-010-a-2020-vision-of-linear-algebra-spring-2020/resources/the-column-space-of-a-matrix/
