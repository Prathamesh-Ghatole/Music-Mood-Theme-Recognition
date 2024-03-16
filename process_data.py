import pandas as pd
import os
from modules.lyric_scraper import get_lyrics
from tqdm import tqdm
from multiprocessing import Pool
import time

# set the path to the data
BASE_DIR = "processed_data/"
ANNOTATIONS_FILE = os.path.join(BASE_DIR, "CAL500_noAudioFeatures/hardAnnotations.txt")
SONGNAMES_FILE = os.path.join(BASE_DIR, "CAL500_noAudioFeatures/songNames.txt")
VOCAB_FILE = os.path.join(BASE_DIR, "CAL500_noAudioFeatures/vocab.txt")

# Multiprocessing params
N_PROCESSES = 10


def process_annotations():
    # read the data
    annotations = pd.read_csv(ANNOTATIONS_FILE, header=None)
    vocab_file = pd.read_csv(VOCAB_FILE, sep="\t", header=None)
    songnames = pd.read_csv(SONGNAMES_FILE, sep="\t", header=None)

    # clean data
    annotations.index = songnames[0]
    annotations.columns = vocab_file[0]
    annotations

    # write data
    annotations.to_csv(os.path.join(BASE_DIR, "CLEANED_cal500_annotations.csv"))

    return annotations


def fetch_lyrics():
    songnames = pd.read_csv(SONGNAMES_FILE, sep="\t", header=None, names=["original"])
    songnames_clean = (
        songnames["original"].str.replace("_", " ").str.replace("-", " - ")
    )

    og_name_lookup = dict(zip(songnames_clean, songnames["original"]))

    def fetch_lyrics_from_series(songnames_series):
        with Pool(N_PROCESSES) as p:
            # Use the pool to apply the fetch_lyrics function to each song in parallel
            fetched_lyrics = list(
                tqdm(p.imap(get_lyrics, songnames_series), total=len(songnames_series))
            )
            return zip(songnames_series, fetched_lyrics)

    fetched_lyrics = fetch_lyrics_from_series(songnames_clean)

    counter = 0
    for songname_clean, item in fetched_lyrics:

        file_name = og_name_lookup.get(songname_clean) + ".txt"

        lyrics_dir = os.path.join(BASE_DIR, "lyrics")
        if not os.path.exists(lyrics_dir):
            os.makedirs(lyrics_dir)
        with open(os.path.join(lyrics_dir, file_name), "w") as f:
            f.write(item["lyrics"])

        counter += 1
    return counter


def main():
    print("Processing annotations...")
    process_annotations()

    print("Fetching lyrics...")
    start = time.monotonic()
    counter = fetch_lyrics()
    time_taken = time.monotonic() - start

    print(f"fethced {counter} lyrics in {time_taken:.2f} seconds")


if __name__ == "__main__":
    main()
