from setuptools import setup,find_packages;

HYPHEN_DOT="-e ."

def find_requirements(str_path):
    with open(str_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("/n","") for req in requirements]
        if HYPHEN_DOT in requirements:
            requirements.remove(HYPHEN_DOT)
    return requirements

setup(
    name="Mlproject",
    version="0.1",
    author="Sivanesan",
    author_email="ssivanesan1812@gmail.com",
    packages=find_packages(),
    install_requires=find_requirements("requirements.txt"),



)