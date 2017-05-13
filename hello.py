age = 28
if (age > 18):
	print("you can vote")
	print ("welcome to the world of adults")
else:
	print("you are not allowed to vote")
	print("i want to vote")
print("kata is my name")

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
	
def table(num):
	for i in range(1,11):
		print(i*num)
		
def hello():
	print("hello")

print("TABLE OF 3")
table(3)
