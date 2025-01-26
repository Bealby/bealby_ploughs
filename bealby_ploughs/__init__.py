# my_package/__init__.py
__version__ = '0.1.0'

def get_version():
    from bealby_ploughs import __version__  # Ensure this import works
    return __version__
