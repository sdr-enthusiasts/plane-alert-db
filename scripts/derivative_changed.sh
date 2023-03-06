# Check if the derivative files have changed.
main_database_files=("plane-alert-db.csv", "plane-alert-pia.csv", "plane-alert-twitter-blocked.csv", "plane-alert-ukraine.csv", "plane_images.txt")

files_changed=$(gh pr view 99 --json files -q '.files[].path' | grep '.csv')
if 
