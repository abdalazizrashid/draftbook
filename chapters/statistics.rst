Statistcal Modeling
###################

Statistcal modeling is a mathematical structure to imitates and approximate the generative process.

The objective of statistcal modeling
=====================================

  * Quantify uncertainty
  * Inference
  * Measure support for hypotheses
  * Predication

Building a statistcal model is a process and each step should be taken carefully.



Statistcal modeling process
============================

  1. Understand the problem
  2. Plan and collect the data
  3. Explore and visualize the data
  4. Postulate the model
      The model should be a balance between complexity and generalizability, this 
      often known as **Bias Variance Tradeoff**.
  5. Fit the model
  6. Check the model
  7. Goto step 4 and repeat
  8. Use the model


Bayesian Model
==============
Let's say we have a dataset of men height collected by a survey, clearly it's almost impassible 
to collect the genetic information that explain the variability in these men heights. We only 
have the men height available to us, to account for variablilty we might assume that the men 
height follow a normal distribution.


.. math::
    y_i = \mu + \epsilon_i\\
    \epsilon_i \overset{iid}{\sim} \mathcal{N}(0, \sigma^2)\\

Or it can be written as:

.. math::
    y_i \overset{iid}{\sim} \mathcal{N}(\mu, \sigma^2)


The main components in Bayesian method:
Robert the Doll
1. Likelihood $p(y|\theta)$
2. Prior $p(\theta)$
3. Posterior:

.. math::
  \begin{align}
  p(\theta | y) &= \frac{p(\theta, y)}{p(y)}\\
  &= \frac{p(\theta, y)}{\int p(\theta, y)d \theta}\\
  &= \frac{p(y| \theta) p(\theta)}{\int p(y|\theta)p(\theta)d\theta}
  \end{align}

Now our model is:

.. math::
  \begin{align}
     y_i | \mu, \sigma^2  &\overset{iid}{\sim} \mathcal{\mu, \sigma^2}  \\
     p(\mu, \sigma^2) &= p(\mu)p(\sigma^2) \\
     \mu &\sim \mathcal{N}(\mu_o, \sigma^2_o)  \\
     \sigma^2 &\sim InverseGamma(\nu_o, \beta_o)  \\
  \end{align}


We can assume independance in the prior and still get dependance in the posterior
The conjugate prior of $\mu$ if we know the value of $\sigma^2$ is a normal distribution,
and the conjugate prior for $\sigma^2$ when the $\mu$ is know is the $InverseGamma$ distribution.


.. warning:: This graph is just a placeholder


.. graphviz::

     digraph foo {
      node [shape = doublecircle]; y1 y2 yn;
	    node [shape = circle];
      "mu" -> "y1";
      "mu" -> "y2";
      "mu" -> "yn";
      "sigma^2" -> "y1";
      "sigma^2" -> "y2";
      "sigma^2" -> "yn";
      "y2" -> "yn";

   }

.. image:: ../images/model_1.png
  :width: 400
  :alt: Graphical represenation showing the observed random variable and the parameters.


.. tikz::
   :libs: arrows,positioning

   [every node/.style={font=\ttfamily\scriptsize,text height=1.5ex,text depth=.8ex},
    var/.style={draw,circle,inner sep=0},
    reentrancy/.style={draw=none,fill=none,text height=1ex,text depth=0},
    proc/.style={-latex,every node/.style={font=\ttfamily\tiny}},
    top/.style={label={[font=\ttfamily\tiny,anchor=base,yshift=.5ex]above:top}}]
   \node[draw=none] (X) {};
   \node[below=0ex of X] (P) {PENMAN};
   \node[right=8em of P] (T) {Tree};
   \node[right=8em of T] (G) {Graph};
   (P) -- (T) -- (G);

   \node [below=5ex of P,xshift=1em,draw=none,text badly ragged,
          label={[align=left]below:(a / alpha\\~~~:ARG0 (b / beta)\\~~~:ARG0-of (g / gamma\\~~~~~~:ARG1 b))}]
         (Pa) {};

   \coordinate[top,below=5ex of T] (TTop);
   \node[var,below=2ex of TTop] (Ta) {a};
   \node[var,below=4ex of Ta,xshift=-1.5em] (Tb) {b};
   \node[var,below=4ex of Ta,xshift=1.5em] (Tg) {g};
   \node[reentrancy,below=4ex of Tg] (Tb2) {b};
   \draw[-latex] (TTop) -- (Ta);
   \draw[-latex] (Ta) -- (Tb) node [midway,left] {:ARG0};
   \draw[-latex] (Ta) -- (Tg) node [midway,right] {:ARG0-of};
   \draw[-latex] (Tg) -- (Tb2) node [midway,right] {:ARG1};

   \coordinate[top,below=5ex of G] (GTop);
   \node[var,below=2ex of GTop] (Ga) {a};
   \node[var,below=3ex of Ga,xshift=-3em] (Gb) {b};
   \node[var,below=6ex of Ga] (Gg) {g};
   \draw[-latex] (GTop) -- (Ga);
   \draw[-latex] (Ga) -- (Gb) node [near start,left] {:ARG0};
   \draw[-latex] (Gg) -- (Ga) node [midway,right] {:ARG0};
   \draw[-latex] (Gg) -- (Gb) node [near start,below left] {:ARG1};


.. tikz::
  :libs: graphs,graphdrawing.layered

  \tikz \graph [layered layout] {
  Hello -> World -> "$c^2$";
  World -> "$\delta$" -> Hello;
  };
