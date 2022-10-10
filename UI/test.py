from main import *
sys.argv = sys.argv
sys.argv = sys.argv[1]

print('full Original' + sys.argv)
v = main(sys.argv)
print(v)
print(type(v))
