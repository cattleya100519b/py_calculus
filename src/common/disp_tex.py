from IPython.display import display, Math
from sympy import latex
from sympy.core import Basic


def disp_tex(str_tex: str | Basic) -> None:
    """
    Display LaTeX string in Jupyter Notebook.

    Parameters
    ----------
    str_tex : str or sympy.core.basic.Basic
        LaTeX string to display.

    """
    # print(type(str_tex))

    if isinstance(str_tex, Basic):
        str_tex = latex(str_tex)

    display(Math(str_tex))
    