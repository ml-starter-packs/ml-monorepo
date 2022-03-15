python_sources(
    name="lib",
    description="resize",
    dependencies = [
        "3rdparty/python:opencv-python",
        "3rdparty/python:numpy",
        "src/python/base:lib"
    ]
)

python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="resize",
        version="0.0.1",
        description="resize package",
    )
)

files(
    name="sample_image",
    sources=[
        "sample_data/*",
    ]
)

python_tests(
    name="tests",
    dependencies = [
        ":lib",
        ":sample_image",
    ]
)
