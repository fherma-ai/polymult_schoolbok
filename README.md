# Polynomial Multiplication — Schoolbook

> **Reference solution by the FHERMA team** · answers
> [`polynomial-multiplication` / `negacyclic@1.0.0`](https://fherma.io/kernels/polynomial-multiplication/specifications/negacyclic)
> on the FHERMA kernel catalogue.

`c = a·b` in the negacyclic ring `Z_q[X]/(X^N + 1)`, computed straight from the
definition: every coefficient of `a` against every coefficient of `b` — `O(N²)`
multiplications of `W`-bit integers — then the negacyclic fold (`X^N = −1`) and
one reduction modulo `q` per coefficient. The operands are public: this is raw
compute, not encrypted. A **correctness baseline**, not a competitive entry — at
`N = 65,536` it is far too slow to win, where a real entry uses a
number-theoretic transform.

```text
kernel polymul<
    N: u32,                    // ring dimension (a power of two)
    W: u32,                    // coefficient width in bits (~ log2 q)
    L: u32 = (W + 31) / 32,    // limbs per coefficient — derived
    q: tensor<L x u32> (N, W), // modulus, derived from (N, W); given at setup
>(
    %a: tensor<N x L x u32>,   // input polynomials, coefficients in [0, q)
    %b: tensor<N x L x u32>,
) -> %c: tensor<N x L x u32>   // a·b in Z_q[X]/(X^N + 1)
```

## Layout

| | |
| --- | --- |
| [`solution/`](solution/) | the measured project: `solve.py` (`init` / `run` / `free`), `fherma.toml`, generated harness |
| [`solution/README.md`](solution/README.md) | what it does and how to run |

## Running it

```sh
cd solution
python main.py <point-dir>
```

The point directory is one the specification's testing bundle produces (`make`):
it holds the point, the cases and `point/q.bin`. At measurement the platform lays
its own copy of every generated file over the clone — the only authored file is
`solve.py`.

## License

MIT.
