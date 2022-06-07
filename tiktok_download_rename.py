import os
import time


def next_number(n):
    return n + 1


# rename all files downloaded from tiktok
def rename_files(path, n):
    for file in os.listdir(path):
        if file.endswith(".mp4") and not file.startswith("t"):
            # time.sleep(0.1)
            # rename to t#.mp4
            # os.rename(os.path.join(path, file), os.path.join(path, "t" + next_number(n)) + ".mp4")

            # rename to tn.mp4 with n being an incremental number
            os.rename(os.path.join(path, file), os.path.join(path, "t" + str(next_number(n)) + ".mp4"))

            return True

if __name__ == "__main__":
    path = r"C:\Users\gioma\Downloads\Tiktoks"
    n = 485   # n of last video downloaded
    while True:
        if rename_files(path, n):
            n += 1
            