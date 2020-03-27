# Multiplicative-Inverse
The program calcs the multiplicative inverse of a number in mod m world.
In mathematics, in particular the area of number theory, a modular multiplicative inverse of an integer a is an integer x such that the product ax is congruent to 1 with respect to the modulus m.[1] In the standard notation of modular arithmetic this congruence is written as

    a x ≡ 1 ( mod m )

which is the shorthand way of writing the statement that m divides (evenly) the quantity ax − 1, or, put another way, the remainder after dividing ax by the integer m is 1. If a does have an inverse modulo m there are an infinite number of solutions of this congruence which form a congruence class with respect to this modulus. Furthermore, any integer that is congruent to a (i.e., in a's congruence class) will have any element of x's congruence class as a modular multiplicative inverse. Using the notation of w ¯ {\displaystyle {\overline {w}}} {\displaystyle {\overline {w}}} to indicate the congruence class containing w, this can be expressed by saying that the modulo multiplicative inverse of the congruence class a ¯ {\displaystyle {\overline {a}}} {\overline {a}} is the congruence class x ¯ {\displaystyle {\overline {x}}} {\overline {x}} such that:

    not a * not x = 1 

where the symbol ⋅ m {\displaystyle \cdot _{m}} {\displaystyle \cdot _{m}} denotes the multiplication of equivalence classes modulo m.[2] Written in this way the analogy with the usual concept of a multiplicative inverse in the set of rational or real numbers is clearly represented, replacing the numbers by congruence classes and altering the binary operation appropriately.

As with the analogous operation on the real numbers, a fundamental use of this operation is in solving, when possible, linear congruences of the form,

    a x ≡ b ( mod m )

Finding modular multiplicative inverses also has practical applications in the field of cryptography, i.e. public-key cryptography and the RSA Algorithm.[3][4][5] A benefit for the computer implementation of these applications is that there exists a very fast algorithm (the extended Euclidean algorithm) that can be used for the calculation of modular multiplicative inverses. 
exemple : 
if (x * a) % m == 1:
  a is a multiplicative inverse of x in modulos m world
