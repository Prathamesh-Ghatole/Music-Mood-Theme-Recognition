"""
## Extracting Relevant Dataset from Complete Dataset
"""

import os
import tarfile

DATASET_1_TAR = "data/cal500data/CAL500_noAudioFeatures.tar.gz"
DATASET_1_TAR_OUTPUT = "processed_data/CAL500_noAudioFeatures/"

DATASET_2 = "data/cal500data/cal500_song_tag_annotations.txt"
DATASET_2_OUTPUT = "processed_data/"


def extract_tar_file(tar_file_path, destination_dir):
    # Validate file paths
    if not os.path.exists(tar_file_path):
        raise FileNotFoundError(f"Tar file '{tar_file_path}' not found.")

    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Open the tar file
    with tarfile.open(tar_file_path, "r") as tar:
        # Extract all the files to the destination directory
        tar.extractall(destination_dir)

    print("Extraction complete!: ", tar_file_path)


def copy(file_path, output_dir):
    # Validate file paths
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    # Create the destination directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Copy the file to the destination directory
    os.system(f"cp {file_path} {output_dir}")

    print("Copy complete!: ", file_path)


def main():
    # Extract the tar file
    extract_tar_file(DATASET_1_TAR, DATASET_1_TAR_OUTPUT)

    # Copy the second dataset
    copy(DATASET_2, DATASET_2_OUTPUT)


if __name__ == "__main__":
    main()
