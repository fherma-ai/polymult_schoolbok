# Polynomial Multiplication — Schoolbook

A reference implementation of [`polynomial-multiplication/negacyclic@1.0.0`](https://fherma.io/kernels/polynomial-multiplication) for the FHERMA catalogue.

## What it does

Computes `c = a · b` in the negacyclic ring `Z_q[X] / (X^N + 1)` straight from the
definition:

1. every coefficient of `a` against every coefficient of `b` — `O(N²)` multiplications of
   `W`-bit integers;
2. the negacyclic fold, `X^N = -1`, so a term of degree `N + k` lands on degree `k` with its
   sign flipped;
3. one reduction modulo `q` per output coefficient.

`q` is fixed for the benchmark point, so it is read once in `init`, before timing starts. The
timed `run` does only the multiplication.

This is a **correctness baseline** — the exponent other implementations are measured against,
not a competitive entry. At `N = 65,536` it is far too slow to win; a real entry uses a
number-theoretic transform.

## Interface

The parameters and coefficient layout are defined by the specification. Coefficients are `W`-bit
integers in `[0, q)`, each stored as `L = ceil(W / 32)` little-endian `u32` limbs;
`a`, `b`, `c` are `tensor<N × L × u32>`.

## Run it

```
python main.py <point-directory>
```

The directory is one the specification's testing bundle produced (`make`): it holds the point,
the cases, and `point/q.bin`. The answer is written to `out/`.
