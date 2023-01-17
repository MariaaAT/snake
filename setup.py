from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


def licence():
    with open("LICENCE") as lic:
        return lic.read()


setup(
    name='snake',
    version='0.0.1',
    description="Simple snake game code",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MariaaAT/snake",
    author="María Andrés",
    author_email="mat9296@gmail.com",
    license=licence(),
    keywords="snake",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["snake", "button?"],
    install_requires=[
        'pygame'
    ],
    include_package_data=True
)
