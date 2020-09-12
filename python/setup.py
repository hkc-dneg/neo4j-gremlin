
from setuptools import find_packages, setup

setup(
    name="neo4j_gremlin",
    version="0.0.1",
    packages=find_packages("src/"),
    package_dir={"": "src/"},

    install_requires=[
        "gremlinpython==3.4.7"
    ]
)
