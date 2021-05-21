from setuptools import setup, find_packages

setup(
    name="high-dim-es-rl",
    version="0.0.4",
    packages=["high_dim_es_rl"],
    install_requires=["numpy",
                      "matplotlib",
                      "scipy",
                      "tensorflow",
                      "keras",
                      "gym"],
)
