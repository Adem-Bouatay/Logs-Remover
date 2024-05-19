import sys

def checkExtension(fileName):
    extension = fileName.split(".")
    if extension[1] != "js":
        raise Exception("Files must be .js files!!")


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file2.js> <file2.js> ...")
        sys.exit(1)
    
    arguments = sys.argv[1:]
    print(f"Arguments: {arguments}")
    for arg in arguments:
        try:
            checkExtension(arg)
            file = open(arg, 'a+')
            print(file.read())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()