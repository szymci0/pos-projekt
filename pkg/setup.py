from setuptools import find_packages, setup

requirements = """
pip>=21.3.1
setuptools>=56
wheel==0.37.0
pandas<2
numpy
pre-commit
flake8==3.8.3
black==21.9b0
coverage
pyarrow
pytest
pytest-cov
feather-format
python-dotenv
click==7.1.2
"""

setup(
    name="pos_pkg",
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "write_to": "../version.txt",
        "root": "..",
        "relative_to": __file__,
    },
    packages=find_packages(),
    install_requires=requirements,
    # include_package_data: to install data from MANIFEST.in
    include_package_data=True,
    zip_safe=False,
)
