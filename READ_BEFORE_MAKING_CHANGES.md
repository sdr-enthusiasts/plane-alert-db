# Read before making changes

Please only suggest/make any changes to the following files:

- [plane-alert-db.csv](plane-alert-db.csv): A list of interesting aircraft with tags, categories and links.
- [plane-alert-pia.csv](plane-alert-pia.csv): A list that contains PIA planes.
- [plane-alert-ukraine.csv](plane-alert-ukraine.csv): A list with Ukrainian planes.
- [plane_images.csv](plane_images.csv): A accompanying list that contains aircraft images.

All other files are generated from this file using the [.github/workflows/create_db_derivatives.yaml](.github/workflows/create_db_derivatives.yaml) GitHub action, and if you do not make your changes there, they will be overwritten and lost.

Note: As Twitter has almost entirely withdrawn API support for free users, we no longer create a separate CSV for use with Twitter bots.
