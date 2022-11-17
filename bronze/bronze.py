# use windows!

import os

def list_files():
	return os.listdir()

def serve():

	while True:
		cmd = input("enter command:")

		if cmd == "list_files":
			print(list_files())
		elif cmd.startswith("read "):
			filename = cmd.split(" ")[1]
			if "secret" in filename:
				print("hacker detected! nice try!")
			else:
				print(open(filename).read())
		elif cmd.startswith("exit"):
			print("exiting.")
			break
		else:
			print("commands: list_files, read <filename>, exit")


def main():
	serve()

if __name__ == '__main__':
	main()
