from setuptools import setup

with open("requirements.txt") as f:
    all_deps = [x for x in f.read().splitlines() if not x.startswith("#")]

setup(
    name="clive-owen",
    version="0.1.0",
    py_modules=["clive"],
    include_package_data=True,
    install_requires=all_deps,
    entry_points={"console_scripts": ["clive=clive:cli"]},
)
