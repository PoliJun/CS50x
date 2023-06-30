import sys

for arg in sys.argv:
    if len(sys.argv) != 2:
        print("Missing argument")
        # exit(1) means that something went wrong
        sys.exit(1)
    print(arg)
sys.exit(0)
