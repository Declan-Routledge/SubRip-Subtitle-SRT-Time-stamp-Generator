class srtClock:
	def ticker(interval, fileName, fileName2):
		
		sec=[0,0]
		min= [0,0]
		hour=[0,0]
		title = 1
		maxChange = 60 - interval
		file1 = open(fileName, 'r') 
		Lines = file1.readlines()
		for line in Lines:
			#adding the interval to the time sheet
			sec[1] = sec[1] +interval
			#file formatted output
			file2 = open(fileName2, 'a') 
			file2.writelines(str(title)+"\n")
			file2.writelines((str(hour[0]).zfill(2)+':'+str(min[0]).zfill(2)+':'+str(sec[0]).zfill(2)+",000 --> "+ str(hour[1]).zfill(2)+':'+str(min[1]).zfill(2)+':'+str(sec[1]).zfill(2)+",000")+"\n")
			file2.writelines(line+"\n")
			#console formatted output
			print (title)
			print (str(hour[0]).zfill(2)+':'+str(min[0]).zfill(2)+':'+str(sec[0]).zfill(2)+",000 --> "+ str(hour[1]).zfill(2)+':'+str(min[1]).zfill(2)+':'+str(sec[1]).zfill(2)+",000")
			print (line)
			
			# Readying for the clock for the next output line
			title += 1
			sec[0] =sec[1]
			min[0] = min[1]
			hour[0]= hour[1]
			#Minute crossover check
			if sec[1] == maxChange:
				min[1] +=1
				sec[1] = -(interval)
				#Hour crossover check
				if min[1] == 60:
					min[1] = 0
					hour[1] +=1

		pass
	
	fileName = input("File Name please (w/ extension eg.txt):")
	print (fileName)
	interval1 = input("Please provide a time interval for subtitles \nbetween 1-6 (Seconds) recommended 2: ")
	interval = int(interval1)
	fileName2 = input("File Name please (w/ extension eg.txt):")	
	ticker(interval, fileName, fileName2)
