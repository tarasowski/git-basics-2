def main(event, ctx):
	print("3")
	print("second once")
	print("from git")
	return "success"

def second_fn(args):
	return {"message": "success"}

def add(num1, num2):
	result = num1 + num2
	return result