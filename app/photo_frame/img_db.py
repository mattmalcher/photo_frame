import sqlite3
import os
import exifread


def init_db(db_loc: str):
    """Initialise Image Database
    Create an SQLite Database with an images table
    """
    print("Creating Photo DB")
    con = sqlite3.connect(db_loc)
    cur = con.cursor()

    # Create table
    cur.execute(
        """CREATE TABLE images
                (path text, fname text, date text)"""
    )

    con.commit()
    con.close()


def find_images(path, ftypes=[".jpg", ".jpeg"]):
    """Find Images
    Iterate over the images in path and its subdirectories, and populate the
    image database with them.

    path - folder to look in
    ftypes - filetypes to consider - case insensitive.
    """

    for root, dirs, files in os.walk(path):

        full_paths = [
            os.path.join(root, f)
            for f in files
            if os.path.splitext(f)[1].lower() in ftypes
        ]

        return full_paths


def get_date_taken(img_pth):

    with open(img_pth, "rb") as fh:
        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags.get("EXIF DateTimeOriginal")
    return dateTaken
