s = "abbcddeeffffcccddddggggghhhiaajjjkk"
print(sorted(set(s)))
for x in sorted(set(s)):
	i = 1;

	while x * i in s:
		i += 1

	print (x, "-", i - 1)