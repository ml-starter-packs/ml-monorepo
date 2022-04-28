# MVP (Minimum Viable Pants)

Even though [pants](https://www.pantsbuild.org/) provide detailed documentation, it lacks a beginner friendly monorepo where users can interact to explore its key concepts. The goals of this repo are:
* To provide a minimal example to showcase pants.
* Lay the foundations for a generic monorepo which can be carried over to other projects.    

## Repository Structure
This monorepo represents the products of a video editing services which contains the following packages:
* _base_: The package shared across different services.
* _resize_: The service to resize a provided video input.
* _track_: The service to track faces in a provided video.

## Package Structure
Each package contains three main files:
* `BUILD`: File used by pants to identify which files are for library and distribution and which ones are for testing.
* `core.py`: The code for the package.
* `test_core.py`: Unit tests for the package. The `sample_data` folder can be created by running `make pull`. The contents of this folder are not too important and can contain any image as long as they are labeled as `sample_imageN.png`, where N is a number.

## Configuring Pants
The `pants.toml` file can be used to alter its behavior.

## Interacting with Pants
We have created a Makefile to ease the use of pants:
* `make install`: Install all the packages in this repo.
* `make format`: Format underlying code using black, isort, flake8 and mypy.

## Extras
We have also provided the functionality to create a single documentation that provides seperate pages for all its repositories. 
