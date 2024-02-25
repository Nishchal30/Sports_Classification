from setuptools import setup, find_packages

# var = "-e ."

__version__ = "0.0.0"

REPO_NAME = "Sports_Classification"
AUTHOR_USER_NAME = "Nishchal30"
SRC_REPO = "src/Sports_Classification"
AUTHOR_EMAIL = "nishchaljinturkar30@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    # package_dir={"":"src"},
    packages=find_packages()
)
