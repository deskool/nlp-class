import random as random


# Instructions if you see zeros getting printed, run it again.

# The list of all students:
students = ['alfadhl2',
'asnanivi',
'chenboc1',
'chenha43',
'collie89',
'cozzoaus',
'dikbayir',
'durgaraj',
'hawki235',
'huynshen',
'kenne476',
'khanahm2',
'kimmic16',
'leesa108',
'bruincam',
'liucha39',
'lotrecks',
'mathonha',
'pandyas6',
'patelab1',
'shenruo2',
'shomalij',
'stanto85',
'vaddine2',
'wanggu22',
'yanzhenz',
'bixiz',
'zhang874']

students = [student + '@msu.edu' for student in students]

all_pairs  = []
pair_taken = []
for student_a in students:
	for student_b in students:
		if student_a[0:5] > student_b[0:5]:
			all_pairs.append([student_a, student_b])
			pair_taken.append(0)

random.shuffle(all_pairs)

#print(len(pair_taken))

homework = {}
for i in range(0,17):
	
	unique_pairs = 0
	while unique_pairs < (len(students) / 2):
		print(unique_pairs)
		
		
		random.shuffle(students)

		matched, homework[i] = [],{}
		unique_pairs = 0    
		# For each of the students
		for student in students:

			# if we have not matched this person yet...		
			if student not in matched:
				
				# cycle through the pairs
				for j,pair in enumerate(all_pairs):

					# if this student is in the pair
					if student in pair:

						# if the pair has never been assigned before...
						if pair_taken[j] == 0:

							# and both parties have not yet been paired...
							if (pair[0] not in matched) and (pair[1] not in matched):
							
								# Add the student to the dict
								homework[i][pair[0]] = pair[1]
								pair_taken[j] = 1 
								matched      += pair 
								unique_pairs += 1
							
					

print(homework)
