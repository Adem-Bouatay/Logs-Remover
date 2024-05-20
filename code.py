import sys

def checkExtension(fileName):
    extension = fileName.split(".");
    if extension[1] != "js":
        raise Exception("Files must be .js files!!");
    
def logRemover(fileLines):
    newFileContent = [];
    for line in fileLines:
        if "console.log" in line:
            content = line.split(";");
            content = [l for l in content if "console.log" not in l];
            content = ';'.join(content);
            newFileContent.append(content);
        else:
            newFileContent.append(line);
    return ''.join(newFileContent);

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file2.js> <file2.js> ...")
        sys.exit(1)
    
    arguments = sys.argv[1:];
    print(f"Arguments: {arguments}");
    for arg in arguments:
        try:
            checkExtension(arg);
            file = open(arg, 'r');
            lines = file.readlines();
            file.close();
            file = open(arg, 'w');
            file.write(logRemover(lines));
            file.close();            
        except Exception as e:
            print(e);
        except IOError as e:
            print(e);

if __name__ == "__main__":
    main();