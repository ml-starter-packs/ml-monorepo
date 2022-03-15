python_sources(
    name="lib",
    description="base",
    dependencies = [
        "3rdparty/python:opencv-python",
        "3rdparty/python:numpy",
    ]
)

python_distribution(
    name="dist",
    dependencies=[":lib"],
    wheel=True,
    sdist=True,
    provides=setup_py(
        name="base",
        version="0.0.1",
        description="base package",
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
