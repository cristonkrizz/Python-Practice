print("Enter the units consumed")
u=int(input())
if u<=150:
	print("Rate Rs:",u*3)
if u>=151 and u<=350:
	print("Rate Rs:",(450+100+((u-150)*3.75)))
if u>=351 and u<=450:
	print("Rate Rs:",(1550+((u-350)*4)))
