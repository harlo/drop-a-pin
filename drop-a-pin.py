import os, re
from time import sleep

sleepy_time = 10
pipe_location = "/home/user/Documents/a_pipe"

def main():
	# if the pipe is already created, you will throw an error
	# so let's delete the old pipe before starting a new one

	if os.path.exists(pipe_location):
		os.remove(pipe_location)

	try:
		os.mkfifo(pipe_location)
	except Exception as e:
		print(e, type(e))

	# this is an infinite loop!
	# this program will continually check the pipe for new info

	while True:
		with open(pipe_location) as FIFO:
			while True:
				sleep(sleepy_time)
				fifo_data = FIFO.read()
				
				if len(fifo_data) == 0:
					break

				print("FIFO says:\n{0}".format(fifo_data))				

if __name__=="__main__":
	main()