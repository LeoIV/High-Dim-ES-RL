from setuptools import setup, find_packages

setup(
    name="high-dim-es-rl",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["numpy",
                      "matplotlib",
                      "scipy",
                      "tensorflow",
                      "keras",
                      "gym"],
)
