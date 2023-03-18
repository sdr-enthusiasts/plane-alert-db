# Read before making changes

Please only suggest/make any changes to the following files:

- [plane-alert-db.csv](plane-alert-db.csv): A list of interesting aircraft with tags, categories and links.
- [plane-alert-pia.csv](plane-alert-pia.csv): A list that contains PIA planes.
- [plane-alert-twitter-blocked.csv](plane-alert-twitter-blocked.csv): A list of aircraft that will cause your Twitter account to be banned when used with `docker-planefence`. **Please use it with care**.
- [plane-alert-ukraine.csv](plane-alert-ukraine.csv): A list with Ukrainian planes.
- [plane_images.txt](plane_images.txt): A accompanying list that contains aircraft images.

All other files are generated from this file using the [.github/workflows/create_db_derivatives.yaml](.github/workflows/create_db_derivatives.yaml) GitHub action, and if you do not make your changes there, they will be overwritten and lost.
