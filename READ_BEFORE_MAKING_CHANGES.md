# Read before making changes

Please only suggest/make any changes to the following files:

- [plane-alert-db.csv](plane-alert-db.csv): This is the main database file. All non-image changes should be done here.
- [plane-alert-pia.csv](plane-alert-pia.csv): This list contains PIA planes.
- [plane-alert-twitter-blocked.csv](plane-alert-twitter-blocked.txt): This source file contains planes that will cause your Twitter account to be banned. Please use it with care.
- [plane-alert-ukraine.csv](plane-alert-ukraine.csv): This list contains Ukrainian planes.
- [plane_images.txt](plane_images.txt): You can add plane images in this source file.

All other files are generated from this file using the [.github/workflows/create_db_derivatives](.github/workflows/create_db_derivatives) GitHub action, and if you do not make your changes there, they will be overwritten and lost.
