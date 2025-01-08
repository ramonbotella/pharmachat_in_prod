"""**Top level variables**."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
    """Package version.

    This string contains the package version and can be imported as:

    .. doctest::

        >>> from pharmachat import __version__

    """
except PackageNotFoundError:
    pass

__all__ = ["__version__"]