# OD_Designs
A collection of previously unknown Orthogonal Designs as listed in the appendices of "Orthogonal Designs Hadamard Matrices, Quadratic Forms and Algebras" by Jennifer Seberry.

From the introduction of the above book:

An orthogonal design of order $n$, type $(s_1, \dots, s_l)$, denoted, OD(n; $s_1, \ldots, s_l)$, $s_i$ positive integers,is an $n \times
n$ matrix with entries from $\{0, \pm x_1, \dots, \pm x_l\}$ (the $x_i$ commuting indeterminates) satisfying:

$XX^T=(\sum_{i=1}^l s_i x_i^2) I_n$

Each json file encodes an orthogonal design. For example, `od24_1_1_1_1_2_5_5_8.json` encodes an $OD(24;1,1,1,1,2,5,5,8)$ with $1$ replacing $x_1$  ($-1$ replacing $-x_1$), $2$ replacing $x_2$ and so on.

These designs were all produced via searches using `pl_search_cpp` with various techniques used to reduce the search space. For ODs with at least three singleton indeterminates the code was checked on known order 24 designs with 8 indeterminates with at least 3 being singletons. The code found solutions for all of the known designs. The listed designs where the only ones found from the unknows list, suggesting these were the only ones.

Solutions for the designs $OD(24;1,1,1,1,1,1,1,9)$ and $OD(24;1,1,1,1,1,1,5,5)$ were previously found using different techniques by Andrew Souter.
