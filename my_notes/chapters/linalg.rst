###############
Linear Algebra
###############
The Matrix Alphabet
^^^^^^^^^^^^^^^^^^^^

| $A$ Any Matrix
| $C$ Circulant Matrix
| $C$ Column Matrix
| $D$ Diagonal Matrix
| $F$ Fourier Matrix
| $I$ Identity Matrix
| $L$ Lower Triangular Matrix
| $L$ Laplacian Matrix
| $M$ Markov Matrix
| $M$ Mixing Matrix
| $P$ Projection Matrix
| $P$ Probability Matrix
| $P$ Perumutation Matrix
| $Q$ Orthogonal Matrix
| $R$ Upper Triangular Matrix
| $R$ Row Matrix
| $S$ Symetric Matrix
| $S$ Sample Covariance Matrix
| $T$ Tensor
| $U$ Upper Triangular Matrix
| $U$ Left Singular Vectors
| $V$ Right Singular Vectors
| $X$ Eigenvector Matrix
| $\Lambda$ Eigenvalue Matrix
| $\Sigma$ Singular Value Matrix


Matrices
========
A matrix is a linear function that maps vectors to vectors $A\b{x}=\b{y}$.
Here $A$ is $m\times n, \b{x} \in \bb{R}^n \text{and } y \in \bb{R}^m$. 
A matrix apply a linear transformating that rotate and strech a vector.

.. math::
    \begin{align}
    \textbf{x} &= x_1 \textbf{e}_1 + x_2 \textbf{e}_2 + \dots + x_n \textbf{e}_n
    \\
    f(\textbf{x}) &= f(x_1 \textbf{e}_1 + x_2 \textbf{e}_2 + \dots + x_n \textbf{e}_n)
    \\
    &= f(x_1 \textbf{e}_1) + f(x_2 \textbf{e}_2) + \dots + f(x_n \textbf{e}_n) && \text{Additivity}
    \\
    &= x_1 f(\textbf{e}_1) + x_2 f(\textbf{e}_2) + \dots + x_n f(\textbf{e}_n) && \text{Homogeneity of degree $1$}
    \\
    &= \left[\begin{array}{c|c|c|c} f(\textbf{e}_1) & f(\textbf{e}_2) & \dots & f(\textbf{e}_n) \end{array}\right] \textbf{x}
    \end{align} 
    
The Geometry of Linear Equations
________________________________

Matrix Form
^^^^^^^^^^^

.. math::
  \begin{alignat*}{4}
  &2x-y&&=0\\
  &-x+2y&&=3\\
  &\begin{bmatrix}
    2   &   -1\\
    -1   &    2\\
  \end{bmatrix}
  &\begin{bmatrix}
      x\\
      y\\
  \end{bmatrix}
  &=
  \begin{bmatrix}
    0\\
    3\\
  \end{bmatrix}\\
  &A & \b{x} &= b
  \end{alignat*}

.. warning:: Fix alignment of equations



Row Picture
"""""""""""
.. warning:: Add Row picture plot


Column Picture
""""""""""""""
.. math:: 
  x \begin{bmatrix} 2 \\ -1 \end{bmatrix} +
  y \begin{bmatrix} -1 \\ 2 \end{bmatrix} =
  \begin{bmatrix} 0 \\ 3 \end{bmatrix}

So we need to take the right combination to produce $\begin{bmatrix} 0 \\ 2 \end{bmatrix}$
Let's take $x=1, y=2$. Thus the idea of linear combination is crucial.
If we took all the possible linear combination of $x$'s and $y$'s. What will be the results?
The results would be that we could get any RHS at all, the combination of x 
$\begin{bmatrix} 2\\ -1 \end{bmatrix}$, $\begin{bmatrix} -1\\ 2 \end{bmatrix}$ would fill the 
whole plane.

.. warning:: Add column picture plot

Basically the interpretation of this is to combine the vector $\begin{bmatrix} 2\\ -1 \end{bmatrix}$ 
with $\begin{bmatrix} -1\\ 2 \end{bmatrix}$ with the right amount to find 
$\begin{bmatrix} 0\\ 3 \end{bmatrix}$, in other words it's a **Linear Combination** of the columns.



Matrix Multiplication
=====================
Matrix vector multiplication can be seen in two ways, either as a inner products of the rows or 
combination of the columns.

.. math:: 
  \bf{By rows} \space
  \begin{bmatrix}
  2   &   2\\
  2   &   2\\
  2   &   2\\
  \end{bmatrix}
  \begin{bmatrix}
  x_1\\
  x_2\\
  \end{bmatrix}
  =
  \begin{bmatrix}
  2x_1 + 2x_2\\
  2x_1 + 2x_2\\
  2x_1 + 2x_2\\
  \end{bmatrix}






Elimination
===========

.. math:: 
  \begin{bmatrix}
    1   &   2   &   1\\
    3   &   8   &   1\\
    0   &   4   &   1\\
  \end{bmatrix}
  \rightarrow (\times 3)
  \begin{bmatrix}
    1   &   2   &   1\\
    0   &   2   &   -2\\
    0   &   4   &   1\\
  \end{bmatrix}
  \rightarrow (\times 2)
   \begin{bmatrix}
    1   &   2   &   1\\
    0   &   2   &   -2\\
    0   &   0   &   -5\\
  \end{bmatrix}



Eigen-vectors and Eigen-values
==============================
A square matrix has a special vector for wich it acts as a number: $A\b{s}=\lambda \b{s}$.
These vectors and numbers are called eigen-vectors and eigen-values, and they are an important
property of the matrix.
Since:

.. math:: A \b{s} - \lambda \b{s} = (A - \lambda I) \b{s} = 0
   :label: eigen


is a homogeneous system, it has a non-trivial solutions only if $\text{det}(A - \lambda I)=0$
this gives an $n^{th}$ order algebriac equation to find $\lambda$, and in general there will be $n$
complex roots, of this equation.
For each root, one finds eigen-vectors $\b{s}$.

Example:

.. math:: 
    A &=
    \begin{bmatrix}
        2  & -1 & 0\\
        -1 &  2 & -1\\
        0  & -1 &  2
    \end{bmatrix}\\
    \text{det}(A - \lambda I) &=
    \begin{vmatrix}
    2-\lambda     &     -1        &         0\\
    -1            &   2-\lambda   &         -1\\
    0             &     -1        &       2 - \lambda
    \end{vmatrix}\\
    &=
    \begin{vmatrix}
        0   &   -1-(2-\lambda)^2    &   2-\lambda\\
        -1  &   2-\lambda           &   -1\\
        0   &   -1                  &   2-\lambda\\
    \end{vmatrix}\\
    &=
    \left[(\lambda -2)(1+(\lambda-2))^2 - \lambda + 2 \right]\\
    &= (\lambda - 2 \left[(\lambda -2 )^2-2 \right]=0\\

Therefore $\lambda_1 = 2$ and $\lambda_{2,3} = 2\pm \sqrt{2}$
and for each eigen-value there is an eigen-vector, for example for $\lambda_1 = 2$ we get:

.. math::
    (A-2I)\b{s_1} &=
    \begin{bmatrix}
        0   &   -1    &     0\\
        -1  &   0     &     -1\\
        0   &   -1    &     0
    \end{bmatrix}
    \b{s_1} = 0

Therefore $s_1= \begin{bmatrix} 0   &   1   &   0   \end{bmatrix}^T$, and the
other eigen-vectors $\b{s}_{2,3}=\left[ 1 \pm \sqrt{2} \right]^T$.

From the definition we can deduce the factorization:

.. math::
    AS = S\Lambda

where columns of $S$ are eigen-vectors and $\Lambda$ is a diagonal matrix with $\b{e}-values \lambda 
on it's diagonal If we recall how the matrices multiply this factorization easily follows as a 
shorthand for

.. math::
    \begin{bmatrix}
        \vertbar   &    \vertbar    &            &   \vertbar  \\
        As_1       &    As_2        &   \dots    & As_n  \\
        \vertbar   &    \vertbar    &            &   \vertbar  \\
    \end{bmatrix}
    &=
    \begin{bmatrix}
        \vertbar   &    \vertbar    &            &   \vertbar  \\
        \lambda_1 s_1       & \lambda_2 s_2 & \dots     &   \lambda_n s_n \\
        \vertbar   &    \vertbar    &            &   \vertbar  \\
    \end{bmatrix}
    &=
    \begin{bmatrix}
        \vertbar   &    \vertbar    &            &   \vertbar  \\
         s_1       &    s_2        &   \dots    & s_n  \\
        \vertbar   &    \vertbar    &            &   \vertbar  \\
    \end{bmatrix}
    \begin{bmatrix}
        \lambda_1  &    0              &   \dots \\
        0          &    \lambda_2           & 0  \\
        \vdots          &    0              &   \ddots \\
    \end{bmatrix}

Then, if $S$ is full rank, $A$ can be decomposed as

.. math:: A = S \Lambda S^{-1}

which is called the **Spectral Decomposition**. Not all matrices enjoy this kind of factorization,
but an important class of symmetric matrices does.
Another way of looking at this factorization follows from the fact that $Ax=b$ can be seen as 
expressing the vector $b$ in terms of columns of matrix $A$.

.. math:: b = x_1 a_1 + x_2 a_2 + \dots + x_n a_n

In other words, if columns of $A$ for a basis, this is simply a change of basis formula, expressing
vector $b$ in that new basis, rather than standard basis made of 1's and 0. And $x=A^{-1}b$ are the coordinates of $b$ in that new basis. Indeed, $b$ in the standard basis

.. math:: e_1 =
    \begin{bmatrix}
        1 \\ 0 \\ 0\\ \vdots\\ 0\\
    \end{bmatrix}
    , e_2=
    \begin{bmatrix}
        0 \\ 1 \\ 0\\ \vdots\\ 0\\
    \end{bmatrix}, \dots

is 

.. math:: b =
    \begin{bmatrix}
        b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_n\\
    \end{bmatrix}
    =
    b_1 e_1 + b_2 e_2 + \dots + b_n e_n
 
showing that $b_i$ is the component of b in the direction of $e_i$. And so $x_i$ is similarly
a component of $b$, now is the direction of $a_i$.

Then if we act with $A=S\Lambda S^{-1}$ on $x$ we get 

.. math:: Ax=S\Lambda (S^{-1}x)

This can be interpreted, reading from right to left, as saying that:

1. change the basis to that of the eigen-vectors to find new components of $x$ in that basis as
   $S^{-1}x$;
2. then strech the new coordinates by eigen-values: $\Lambda(S^{-1}x)$;
3. and return to the original basis by multiplying with $S$.



Singular Value Decomposition (SVD)
==================================

.. math::
    A &=U \Sigma V^T\\
    &= \sigma_1 u_1 v_1^T + \sigma_2 u_2 v_2^T + \cdot + \sigma_n u_n v_n^T\\

Where $U \in \bb{R}^{m \times m}, V \in \bb{R}^{n\times n}, \Sigma \in \bb{R}^{m \times n}$, $n $ is the rank, and $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_n$.


Solvability Conditions for Linear Systems
=========================================
Let $A$ be $n \times n$ and consider $Ax=b$. If $A$ is not singular, the this 
system has a unique solution $x=A^{-1}b$. Then the question does a singular matrix have 
a solution? The answer is it depends on the relationship between $A$ and $b$.
$Ax$ is always a combinantion of columns of $A$, no matter what $x$ is. Therefore, for 
$Ax=b$ to have a solution, $b$ must be a combination of columns of $A$. In another word,
$b$ must be in the columns space of $A, b \in C(A)$. This condition on $b$ can be expressed
as an orthogonality condition, as any vector in $C(A)$ must be orthogonal to the left 
nullspace of $A, N(A^T)$. $y^Tb=0$, solvability condition for $Ax=b$, where $A^Ty=0$.
The equation $A^T y=0$ is called the adjoint problem.

Example:

.. math::
    \begin{bmatrix}
        1   &   0   &   2\\
        2   &   2   &   8\\
        0   &  -1   &   -3
    \end{bmatrix}

is singular because $A(:,3)=2A(:,1)+3A(:,2)$. It's left nullspace is spanned by 
$\begin{bmatrix} 1  &   -1   &   -2 \end{bmatrix}$, since $1.row_1 - row_2 - 2.row_3=0$, or:

.. math::
    A^T y=
    \begin{bmatrix}
        1   &   1   &   0\\
        0   &   2   &  -1\\
        2   &   8   &  -3\\
    \end{bmatrix}
    \begin{bmatrix}
        1   \\   -1  \\   -2\\
    \end{bmatrix}
    =
    \begin{bmatrix}
        0   \\   0   \\   0\\
    \end{bmatrix}


Therefore, $Ax=b$ will have a solution only if $b$ satisfies $y^T b = b_1 - b_2 - 2_b3 = 0$.
In fact, if that condition is satisfied, $Ax=b$ will have infinitely many solutions, as one can
add to $x$ the nullspace of $A,Ax_0=0$, so that if $x$ is a solution then $x+x_0$ is also a 
solution, $A(x+x_0)=Ax+Ax_0=b$. This is the **Fredholm alternative**.

All this will boil down to the three fallowing cases:

1. If $Ax=b$ where $A \in \bb{R}^{m \times m}$, and $A$ is singular, the solution is given by
   $x=A^{-1}b$.
2. If $A$ is singular and $b \in C(A)$, in another word it's orthogonal to the left nullspace
   of $b$. There is infinitely many solutions.
3. If $A$ is singular and $b \notin C(A)$, in another word it's not orthogonal to the left nullspace
   of $b$. There is no solution.

