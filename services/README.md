# File Storage


Sets up `apache` and `minio` pointing to the same directory.

This gives you programmatic access to upload / download files and
also the convenience of accessing them through some fully-qualified
domain name.


Note: the default `./data` path is just for example purposes.
In production, you can migrate and edit `./services` as its own
folder with its data directories and container names configured
to your liking.
