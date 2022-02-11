# Mock-company-name (TBD)

This is an educational repository for the fictional company Mock-company-name which provides a range of video editing services. This company store all of their services/products in a monorepo managed by [pants](https://www.pantsbuild.org/). The goal of this repository is to expand on the examples provided in the original pants documentation and show pants's key concepts in a centralized location.


## Repository Structure
This monorepo stores the following packages
* _base_: The repo shared accross different services
* _resize_: The service to resize provided video input to a requested size
* _track_: The service to track faces in a provided video
