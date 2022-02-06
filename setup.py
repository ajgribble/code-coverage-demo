from setuptools import setup, find_packages
from glob import glob
from os.path import basename
from os.path import splitext

setup(
    name="demo",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
