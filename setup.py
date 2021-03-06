import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="report_racing_pkg",
    version="0.0.2",
    author="Anna Katunina",
    author_email="leznevoanna@gmail.com",
    description="A package that reads data from 3 files start.log, end.log and abbreviation and print"
                "report of the top 15 racers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.foxminded.com.ua/anna_katunina/task-6-report-monaco-racing",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
