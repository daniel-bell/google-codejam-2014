import sys
sys.setrecursionlimit(15000)
file_name = sys.argv[1]

# def cookie_recurse(time, cps, c, f, x):
	


with open(file_name, "r") as fin:
	num = int(fin.readline())

	for i in range(num):
		raw_line = fin.readline()
		line = [float(x) for x in raw_line.split(" ")]

		c = line[0]
		f = line[1]
		x = line[2]
		cps = 2
		time = 0
		time_to_target = 0	
		# no_farm_time = cookie_recurse(0, 2, c, f ,x)
		while(True):
			time_to_target = time + (x / cps)

			time_to_farm = (c / cps)
			after_farm_target = (x / (cps + f))

			# print("time_to_target " + str(time_to_target))
			# print("After farm target " + str(time + (after_farm_target + time_to_farm)) + "\n")

			if time_to_target < (time + (time_to_farm + after_farm_target)):
				break
			else:
				cps = cps + f
				time = time + time_to_farm

		print("Case #" + str(i + 1) + ": " + str(round(time_to_target, 7)))