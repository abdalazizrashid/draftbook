Probability
===========

Probability Cheatsheet

===============================================     ================================
Notation symbol                                     Meaning
===============================================     ================================
$\Omega$                                            Sample space
$\omega$                                            Atom
$p(\omega)$                                         Probability measure
$X$                                                 Random variable
$x$                                                 Realization of random variable
$p(X, Y, Z)$                                        Joint distribution
$p(X|Y)=\frac{p(X,Y)}{p(Y)}$                        Conditional Probability
$p(X)=\sum_{y}p(X,Y=y)$                             Marginalization
$p(Y|X) \propto p(X|Y)p(Y)$                         Bayes rule
$X \perp Y \iff p(X,Y)=p(X)p(Y)$                    Independence
$X \perp Y|Z \iff p(X,Y,Z)= p(X|Z)p(Y|Z)$           Conditional independence 
$\bb{E}\right[f(X)\left]=\sim_x f(x)p(x)$           Expectation
$\bb{E}\right[f(X)|Y=y\left]=\sim_x f(x)p(x|y)$     Conditional expectation
===============================================     ================================


General Advice for Linear-Regression Priors
##############################################

* Intercept  :math:`\alpha`
  We have no idea where it might end up so need to use 
  broad Gaussian prior.


* Slope :math:`\beta`: 
  Gaussian centered on zero, scale should be so extreme for
  regularization.

* Scale :math:`\bb{R,Q, Z} \RR \sigma \bold{R}` 
  Uniform with reasonable upper bound, we may use Cauchy or
  exponential for regularization.



