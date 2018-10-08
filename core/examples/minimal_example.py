from webviz import Webviz, Page, SubMenu, Markdown, Html

web = Webviz('Main title', theme='minimal')

ex1 = Page('Example 1')
ex2 = Page('Example 2')
ex3 = Page('Markdown example')

some_content = (r"""

# Markdown support
***

> __You can pass markdown wihin a triple-quotes__<br>
> _Also known as multiline comments_

|First Header  | Second Header  | Third Header |
|:-------------|:-------------: | ------------:|
|Content Cell  | `Content Cell` | Content      |
|Content Cell  | Content Cell   | Content      |

---

    #!python
    def hello():
        print('Hello World')
---
If you want to use math formulas, you have several different options. You can
use double dollar signs:

```
$$ \left(\frac{\sqrt x}{y^3}\right) $$
```

Result: $$ \left(\frac{\sqrt x}{y^3}\right) $$

Or you can wrap it between special commands like this:

```
\begin{equation}
\cos (2\theta) = \cos^2 \theta - \sin^2 \theta \label{my_cos_equation}.
\end{equation}
```

Result:
\begin{equation}
\cos (2\theta) = \cos^2 \theta - \sin^2 \theta \label{my_cos_equation}.
\end{equation}

All equations with labels can easily be referred to in the text as
```\eqref{my_cos_equation}```, resulting in something like
\eqref{my_cos_equation}.


If you want an equation without numbering add "notag":

```
\begin{equation}
\lim_{x \to \infty} \exp(-x) = 0.\notag
\end{equation}
```

Result:
\begin{equation}
\lim_{x \to \infty} \exp(-x) = 0.\notag
\end{equation}

If you want to write multi-line equations aligned on e.g. the equal sign, you
can also do that:

```
\begin{align}
f(x) &= (x+a)(x+b) \\\\
     &= x^2 + (a+b)x + ab
\end{align}
```

Result:
\begin{align}
f(x) &= (x+a)(x+b) \\\\
     &= x^2 + (a+b)x + ab
\end{align}

The & operator indicates what to align on. You can also write in-line equations
or symbols inbetween, like ```\( \alpha \)``` (\( \alpha \)) and
```\( \gamma \)``` (\( \gamma \)).

To prevent build failing because of backslashes, use a rawstring format by
adding `r` in front of the string.

You can read more about the input format
[here](http://docs.mathjax.org/en/latest/tex.html#).

Example:

`formula = Markdown(r'$$x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2b}.$$')`

Renders out to this:

$$x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2b}.$$
""")


ex3.add_content(Markdown(some_content))

submenu1 = SubMenu('Menu 1')
submenu2 = SubMenu('Menu 2')
submenu3 = SubMenu('Menu 3')

submenu1.add_page(ex1)
submenu2.add_page(ex2)
submenu3.add_page(ex3)

web.add(submenu1)
web.add(submenu2)
web.add(submenu3)

web.write_html("./webviz_example", overwrite=True, display=False)
