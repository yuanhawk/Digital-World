def main():
	f = open('lines.txt')	# Returns a File Object
	for line in f:	# Use an iterator
	print(line.rstrip())	# String rstrip(), strips new lines
	
if __name__ == '__main__': main()