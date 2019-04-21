import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="downloader",
    version="0.1.0",
    author="Micah Lee",
    author_email="micah@micahflee.com",
    description="This is a very simple GUI app for learning how to packaging things with flatpak.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3+",
    packages=['downloader'],
    entry_points={
        'console_scripts': [
            'downloader = downloader:main',
        ],
    },
)
