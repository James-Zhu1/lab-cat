'''
This program prints stdin to the screen using O(1) memory.
'''
import sys

def cat(file):
    # Read and write in fixed-size chunks to maintain O(1) memory
    chunk_size = 8192  # 8KB chunk
    while True:
        chunk = file.read(chunk_size)
        if not chunk:
            break
        sys.stdout.buffer.write(chunk)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f)
    else:
        cat(sys.stdin.buffer)
