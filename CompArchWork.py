
import sys



#simple thing to grab command line arguments
print("Starting project \n")
for i in sys.argv:
    print(i, '\n')
    sys.stdout.write(i, '\n')
print(sys.argv[0])