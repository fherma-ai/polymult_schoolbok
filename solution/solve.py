"""Schoolbook multiplication in Z_q[X] / (X^N + 1).

The definition, computed directly: every coefficient of a against every
coefficient of b, then the negacyclic fold, then one reduction each. N^2
multiplications of W-bit integers and nothing saved anywhere.

It is here to be the thing other implementations are faster than. The
interesting question is what happens to the exponent as N grows, and this is
the exponent to beat.
"""
from fherma import Inputs, Outputs, Point, pack, unpack, unpack_one


def init(p: Point):
    """q is fixed for the point and arrives here, before the timed run.

    There is nothing else worth keeping: the work is a double loop whose bounds
    are the only thing the point decides. `p.L` is the limb count the answer is
    packed back into.
    """
    return p.N, p.L, unpack_one(p.q)


def run(state, inp: Inputs) -> Outputs:
    n, limbs, q = state

    # Words to integers at the edge, and back at the other edge. Inside, this is
    # arithmetic on integers and the width has stopped mattering.
    a = unpack(inp.a)
    b = unpack(inp.b)

    product = [0] * (2 * n - 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            product[i + j] += ai * bj

    # X^N = -1 in this ring, so a term of degree N + k is a term of degree k
    # with the sign turned over.
    for degree in range(n, len(product)):
        product[degree - n] -= product[degree]

    return Outputs(c=pack([one % q for one in product[:n]], limbs, "u32"))


def free(state) -> None:
    return None
