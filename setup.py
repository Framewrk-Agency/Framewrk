from setuptools import setup, find_packages

setup(
    name='framewrk',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask'],
    setup_requires=['libsass >= 0.14.5'],
    sass_manifests={
        'app': ('static/scss', 'static/css', '/static/css')
    }
)
