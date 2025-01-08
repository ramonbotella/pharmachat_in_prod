"""**CLI access point**.

With this module we enable the ``python -m pharmachat``
functionality.

The CLI should also be accessible through the command:
``pharmachat``.

"""

from pharmachat.cli import app

if __name__ == "__main__":
    app()