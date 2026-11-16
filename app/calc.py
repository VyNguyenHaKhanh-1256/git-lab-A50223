def add(a, b):
    """Cong hai so a va b."""
    return a + b


def sub(a, b):
    """Tru hai so a va b."""
    return a - b


def div(a, b):
    """Chia a cho b."""
    if b == 0:
        raise ValueError("[ZeroDivision] Loi: chia cho 0")
    return a / b
