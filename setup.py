from distutils.core import setup

setup(
    name='geokit',
    version='0.0.1',
    author='Severin Ryberg',
    url='http://www.fz-juelich.de/iek/iek-3/EN/Home/home_node.html',
    packages = ["geokit"],
    install_requires = [
        "gdal>=2.1.0",
        "numpy>=1.11.2",
    ]
)