from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int, help="time in seconds")
args = parser.parse_args()
print(f'Starting timer of {args.time} seconds')
for _ in range(args.time):
    print(".", end=" ", flush=True)
    sleep(1)
print("\nTimer finished")


###

import subprocess
subprocess.run(["notepad"])