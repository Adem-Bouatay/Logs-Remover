import sys
extenstions = {"js", "py", "ts", "java", "c"};

def checkExtension(fileName):
    extension = fileName.split(".");
    if extension[1] not in extenstions:
        raise Exception(f"Files must be {extenstions} files!!");
    
def logRemover(fileLines, langLog):
    newFileContent = [];
    for line in fileLines:
        if langLog in line:
            content = line.split(";");
            content = [l for l in content if langLog not in l];
            content = ';'.join(content);
            newFileContent.append(content);
        else:
            newFileContent.append(line);
    return ''.join(newFileContent);

def fileManager(arg, langLog):
    file = open(arg, 'r');
    lines = file.readlines();
    file.close();
    file = open(arg, 'w');
    file.write(logRemover(lines, langLog));
    file.close();
    file = open(arg, 'r');
    print(file.read());
    print("done!!")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <file2.js> <file2.js> ...")
        sys.exit(1)
    
    arguments = sys.argv[1:];
    print(f"Arguments: {arguments}");
    for arg in arguments:
        try:
            extension = arg.split(".")[1];
            checkExtension(arg);
            match extension:
                case "js":
                    fileManager(arg, "console.log");
                case "ts":
                    fileManager(arg, "console.log");
                case "py":
                    fileManager(arg, "print");
                case "java":
                    fileManager(arg, "System.out.println");
                case "c":
                    fileManager(arg, "printf");
        except Exception as e:
            print(e);
        except IOError as err:
            print(err);

if __name__ == "__main__":
    main();