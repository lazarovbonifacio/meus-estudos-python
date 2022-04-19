from aula46_3.formatador.formata_real import real as fmt_2_real

def total():
    pass

def desconto(p,d,fmt=False):
    if fmt:
        return fmt_2_real(p - (p * d/100))
    else:
        return p - (p * d/100)


def aumento(p,d,fmt=False):
    if fmt:
        return fmt_2_real(p + (p * d/100))
    else:
        return p + (p * d/100)
