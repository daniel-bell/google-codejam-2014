import sys
file_name = sys.argv[1]

with open(file_name, "r") as f:
	num = int(f.readline())

	for i in range(num):
		first_row = int(f.readline()) - 1
		first_board = list()

		for x in range(4):
			raw_line = f.readline()
			line = [int(x) for x in raw_line.split(" ")]
			first_board.append(line)

		second_row = int(f.readline()) - 1
		second_board = list()
		for x in range(4):
			raw_line = f.readline()
			line = [int(x) for x in raw_line.split(" ")]
			second_board.append(line)

		common_values = [x for x in first_board[first_row] if x in second_board[second_row]];
		if not common_values:
			case_string = "Volunteer cheated!"
		elif len(common_values) > 1:
			case_string = "Bad magician!"
		else:
			case_string = str(common_values[0])

		print("Case #" + str(i + 1) + ": " + case_string) 