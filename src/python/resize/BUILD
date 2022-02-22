python_sources(
    name="lib",
    description="resize",
    dependencies = [
        "3rdparty/python:opencv-python",
        "3rdparty/python:numpy",
        "src/python/base:lib"
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
