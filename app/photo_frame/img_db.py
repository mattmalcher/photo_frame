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
        """CREATE TABLE images (path text primary key, fname text, date text)"""
    )

    con.commit()
    con.close()


def find_images(path, db_loc, ftypes=[".jpg", ".jpeg"]):
    """Find Images
    Iterate over the images in path and its subdirectories, and populate the
    image database with them.

    path - folder to look in
    ftypes - filetypes to consider - case insensitive.
    """
    full_paths = []

    for root, dirs, files in os.walk(path):

        for f in files:

            ext = os.path.splitext(f)[1].lower()
            full_path = os.path.join(root, f)

            if ext in ftypes:

                upsert_image(
                    db_loc, img_path=full_path, fname=f, date=get_date_taken(full_path)
                )


def get_date_taken(img_pth):

    with open(img_pth, "rb") as fh:
        tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags.get("EXIF DateTimeOriginal")
    return dateTaken


def upsert_image(db_loc, img_path: str, fname: str, date: str):
    con = sqlite3.connect(db_loc)
    cur = con.cursor()

    cur.execute(
        """INSERT INTO images(path, fname, date) VALUES(?,?,?)
        ON CONFLICT(path) DO nothing;
        """,
        [img_path, fname, date],
    )

    con.commit()
    con.close()


def get_random_path(db_loc):

    con = sqlite3.connect(db_loc)
    cur = con.cursor()

    cur.execute("SELECT path, fname, date FROM images ORDER BY RANDOM() LIMIT 1")

    con.commit()

    res = cur.fetchone()
    con.close()

    return res
