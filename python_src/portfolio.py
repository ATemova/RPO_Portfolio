"""
Ta modul predstavlja osnovne podatke o portfoliu in izpiše
kratko predstavitev avtorja.
"""

from dataclasses import dataclass


@dataclass
class Portfolio:
    """Predstavlja preprost osebni portfolio.

    Atributi:
        author_name: Ime in priimek lastnika portfolia.
        email: Kontaktni e-naslov.
        github: Povezava do GitHub profila.

    Primer:
        >>> p = Portfolio("Anastasija Temova", "temanastasa@gmail.com", "https://github.com/ATemova")
        >>> p.intro()
        'Hello, I am Anastasija Temova. Contact: temanastasa@gmail.com • GitHub: https://github.com/ATemova'
    """

    author_name: str
    email: str
    github: str

    def intro(self) -> str:
        """Vrne kratek opis portfolia.

        Vrne:
            Niz z osnovnimi informacijami o avtorju.
        """
        return f"Hello, I am {self.author_name}. Contact: {self.email} • GitHub: {self.github}"


def preveri_email(email: str) -> bool:
    """Preveri, ali e-naslov vsebuje znak '@'.

    Argumenti:
        email: E-naslov, ki ga želimo preveriti.

    Vrne:
        True, če e-naslov vsebuje '@', sicer False.
    """
    return isinstance(email, str) and "@" in email