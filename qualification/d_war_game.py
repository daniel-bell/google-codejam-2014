import sys
file_name = sys.argv[1]

def war(n_blocks, k_blocks):
	n_score = 0

	while n_blocks:
		curr_n_block = min(n_blocks)
		n_blocks.remove(curr_n_block)

		k_blocks = sorted(k_blocks)
		curr_k_block = max(k_blocks)
		for i in range(len(k_blocks)):
			if k_blocks[i] > curr_n_block:
				curr_k_block = k_blocks[i]
				break
		k_blocks.remove(curr_k_block)

		if(curr_k_block < curr_n_block):
			n_score += 1

	return n_score

def deceiptful_war(n_blocks, k_blocks):
	n_score = 0

	while n_blocks:
		if max(n_blocks) > max(k_blocks):
			curr_n_block = max(n_blocks)
		else:
			curr_n_block = min(n_blocks)
		n_blocks.remove(curr_n_block)

		# print("N is playing " + str(curr_n_block))

		if curr_n_block < max(k_blocks):
			curr_n_block = max(k_blocks) - 0.0000001

		# print("N is cheating " + str(curr_n_block))

		k_blocks = sorted(k_blocks)
		curr_k_block = max(k_blocks)
		for i in range(len(k_blocks)):
			if k_blocks[i] > curr_n_block:
				curr_k_block = k_blocks[i]
				break
		k_blocks.remove(curr_k_block)

		# print("K is playing " + str(curr_k_block))

		if(curr_k_block < curr_n_block):
			n_score += 1

	return n_score

with open(file_name, "r") as fin:
	num = int(fin.readline())

	for i in range(num):
		blocks = int(fin.readline())
		raw_line = fin.readline()
		n_blocks = [float(x) for x in raw_line.split(" ")]
		n2_blocks = [float(x) for x in raw_line.split(" ")]
		raw_line = fin.readline()
		k_blocks = [float(x) for x in raw_line.split(" ")]
		k2_blocks = [float(x) for x in raw_line.split(" ")]
		# print(n_blocks)
		# print(k_blocks)

		print("Case #" + str(i+1) + ": " + str(deceiptful_war(n_blocks, k_blocks)) + " " + str(war(n2_blocks, k2_blocks)))

		# print("")		