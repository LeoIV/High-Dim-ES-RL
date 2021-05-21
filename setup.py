from setuptools import setup, find_packages

setup(
    name="high-dim-es-rl",
    version="0.0.7",
    packages=["high_dim_es_rl"],
    install_requires=["numpy",
                      "matplotlib",
                      "scipy",
                      "tensorflow",
                      "keras>=2.4.3",
                      "gym"],
)
