import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="client-tracker",
    version="1.0",
    author="Alan Williams",
    author_email="alan.ws@outlook.com",
    description="send notifications to Slack about user usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/theydonthaveit/kiroku-client-tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
