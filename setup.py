from setuptools import setup

from frida_push import __version__

setup(
    name="frida-start",
    version=__version__,
    packages=["frida_start"],
    url="https://github.com/davidpatel0/frida-start",
    license="GPLv3",
    description="Wrapper tool to identify the remote device and push device specific frida-server binary.",
    install_requires=["requests", "frida"],
    entry_points={"console_scripts": ["frida-start = frida_start.command:main"]},
)
