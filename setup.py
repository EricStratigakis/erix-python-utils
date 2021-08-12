from setuptools import setup

setup(
    name="erix-python-utils",
    version='0.0.1',
    author="Eric Stratigakis",
    author_email="enstrati@uwaterloo.ca",
    description='All of my utilities and tools in one place',
    py_modules=["helloworld"],
    package_dir={'':'src'},
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)