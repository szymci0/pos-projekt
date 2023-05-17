from setuptools import find_packages, setup
import os

requirements = """
pandas<2
numpy
requests==2.25.1
click==7.1.2
fastapi==0.63.0
uvicorn==0.13.3
fastapi-users[mongodb,oauth]==5.1.0
mongoengine>=0.22.1
pymongo>=3.11.3
motor==2.3.1
arrow==0.15.8
aiofiles==0.6.0
python-dotenv==0.13.0
httptools
flower==1.0.0
ipython==7.34.0
"""

setup(
    name="pos_api",
    setup_requires=["setuptools_scm"],
    use_scm_version={
        "write_to": "../version.txt",
        "root": "..",
        "relative_to": __file__,
    },
    install_requires=requirements,
    extras_require={"server": [f"pos_pkg=={os.environ.get('PKG_VERSION')}"]},
    packages=find_packages(exclude=['pkg.pos_pkg']),
    include_package_data=True,
    zip_safe=False,
)