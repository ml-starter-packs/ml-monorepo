python_sources(
    name="lib",
    description="base",
    dependencies = [
        "3rdparty/python:opencv-python",
        "3rdparty/python:numpy",
    ]
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
