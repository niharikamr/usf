
import numpy as np
import csv
from collections import defaultdict
import pandas as pd
import statistics

fout_data = open("/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/processed_data/p1_vid_3_20.11.19_18.05.04.bp_processed.csv",'w')
chan = ['Timestamp','POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']
time, af3_theta, af3_alpha, af3_betal, af3_betah, af4_theta, af4_alpha, af4_betal, af4_betah = ([] for i in range(9))
length=0
count=0
i=0

df = pd.read_csv("/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/copy_of_original_data/p1_vid_3_20.11.19_18.05.04.bp.csv", header=0)
#print(df)

df1=df[['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']]
#print(df1)
#print(df1["POW.AF3.Theta"])

for ch in chan:
	if ch=="POW.AF4.BetaH":
		fout_data.write(ch)
	else:
		fout_data.write(ch+",")
fout_data.write("\n")


while i < (len(df1)):
	length=0
#	print("i", i)
#	print("\n")
	for j in range(i, len(df1)):
#		print("j", j
#		print("\n")
		if df1.loc[i, "Timestamp"]==df1.loc[j, "Timestamp"]:
			length=length+1
			time.append(df1.loc[j,"Timestamp"])
			af3_theta.append(df1.loc[j, "POW.AF3.Theta"])
#			print(type(af3_theta))
			af3_alpha.append(df1.loc[j, "POW.AF3.Alpha"])
			af3_betal.append(df1.loc[j, "POW.AF3.BetaL"])
			af3_betah.append(df1.loc[j, "POW.AF3.BetaH"])
			af4_theta.append(df1.loc[j, "POW.AF4.Theta"])
			af4_alpha.append(df1.loc[j, "POW.AF4.Alpha"])
			af4_betal.append(df1.loc[j, "POW.AF4.BetaL"])
			af4_betah.append(df1.loc[j, "POW.AF4.BetaH"])
		else:
			break
	count=count+1
	time_m=statistics.mean(time)
	af3_theta_m=statistics.mean(af3_theta)
	af3_alpha_m=statistics.mean(af3_alpha)
	af3_betal_m=statistics.mean(af3_betal)
	af3_betah_m=statistics.mean(af3_betah)
	af4_theta_m=statistics.mean(af4_theta)
	af4_alpha_m=statistics.mean(af4_alpha)
	af4_betal_m=statistics.mean(af4_betal)
	af4_betah_m=statistics.mean(af4_betah)



	del time[:]
	del af3_theta[:]
	del af3_alpha[:]
	del af3_betal[:]
	del af3_betah[:]
	del af4_theta[:]
	del af4_alpha[:]
	del af4_betal[:]
	del af4_betah[:]

	fout_data.write(str(time_m)+",")
	fout_data.write(str(af3_theta_m)+",")
	fout_data.write(str(af3_alpha_m)+",")
	fout_data.write(str(af3_betal_m)+",")
	fout_data.write(str(af3_betah_m)+",")
		
	fout_data.write(str(af4_theta_m)+",")
	fout_data.write(str(af4_alpha_m)+",")
	fout_data.write(str(af4_betal_m)+",")
	fout_data.write(str(af4_betah_m))
	fout_data.write("\n")
	
	i=i+length
	print(count)
fout_data.close()	
	

#-------------------------------------------------- FOR VIDEO 2 ------------------------------------------------------------


fout_data = open(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/processed_data/p1_vid_3_20.11.19_18.05.04.bp_processed.csv",
	'w')    #------------------------------------------ CHANGE PATH HERE - Participant Video 2  ------------------------------------------
chan = ['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta',
		'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']
time, af3_theta, af3_alpha, af3_betal, af3_betah, af4_theta, af4_alpha, af4_betal, af4_betah = ([] for i in range(9))
length = 0
count = 0
i = 0

df = pd.read_csv(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/copy_of_original_data/p1_vid_3_20.11.19_18.05.04.bp.csv",
	header=0)  #------------------------------------------ CHANGE PATH HERE - Participant Video 2  ------------------------------------------
# print(df)

df1 = df[
	['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha',
	 'POW.AF4.BetaL', 'POW.AF4.BetaH']]
# print(df1)
# print(df1["POW.AF3.Theta"])

for ch in chan:
	if ch == "POW.AF4.BetaH":
		fout_data.write(ch)
	else:
		fout_data.write(ch + ",")
fout_data.write("\n")

while i < (len(df1)):
	length = 0
	#	print("i", i)
	#	print("\n")
	for j in range(i, len(df1)):
		#		print("j", j
		#		print("\n")
		if df1.loc[i, "Timestamp"] == df1.loc[j, "Timestamp"]:
			length = length + 1
			time.append(df1.loc[j, "Timestamp"])
			af3_theta.append(df1.loc[j, "POW.AF3.Theta"])
			#			print(type(af3_theta))
			af3_alpha.append(df1.loc[j, "POW.AF3.Alpha"])
			af3_betal.append(df1.loc[j, "POW.AF3.BetaL"])
			af3_betah.append(df1.loc[j, "POW.AF3.BetaH"])
			af4_theta.append(df1.loc[j, "POW.AF4.Theta"])
			af4_alpha.append(df1.loc[j, "POW.AF4.Alpha"])
			af4_betal.append(df1.loc[j, "POW.AF4.BetaL"])
			af4_betah.append(df1.loc[j, "POW.AF4.BetaH"])
		else:
			break
	count = count + 1
	time_m = statistics.mean(time)
	af3_theta_m = statistics.mean(af3_theta)
	af3_alpha_m = statistics.mean(af3_alpha)
	af3_betal_m = statistics.mean(af3_betal)
	af3_betah_m = statistics.mean(af3_betah)
	af4_theta_m = statistics.mean(af4_theta)
	af4_alpha_m = statistics.mean(af4_alpha)
	af4_betal_m = statistics.mean(af4_betal)
	af4_betah_m = statistics.mean(af4_betah)

	del time[:]
	del af3_theta[:]
	del af3_alpha[:]
	del af3_betal[:]
	del af3_betah[:]
	del af4_theta[:]
	del af4_alpha[:]
	del af4_betal[:]
	del af4_betah[:]

	fout_data.write(str(time_m) + ",")
	fout_data.write(str(af3_theta_m) + ",")
	fout_data.write(str(af3_alpha_m) + ",")
	fout_data.write(str(af3_betal_m) + ",")
	fout_data.write(str(af3_betah_m) + ",")

	fout_data.write(str(af4_theta_m) + ",")
	fout_data.write(str(af4_alpha_m) + ",")
	fout_data.write(str(af4_betal_m) + ",")
	fout_data.write(str(af4_betah_m))
	fout_data.write("\n")

	i = i + length
	print(count)
fout_data.close()



#-------------------------------------------------- FOR VIDEO 3 ------------------------------------------------------------


fout_data = open(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/processed_data/p1_vid_3_20.11.19_18.05.04.bp_processed.csv",
	'w')    #------------------------------------------ CHANGE PATH HERE - Participant Video 3, also add processed after the name------------------------------------------
chan = ['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta',
		'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']
time, af3_theta, af3_alpha, af3_betal, af3_betah, af4_theta, af4_alpha, af4_betal, af4_betah = ([] for i in range(9))
length = 0
count = 0
i = 0

df = pd.read_csv(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/copy_of_original_data/p1_vid_3_20.11.19_18.05.04.bp.csv",
	header=0)  #------------------------------------------ CHANGE PATH HERE - Participant Video 3 ------------------------------------------
# print(df)

df1 = df[
	['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha',
	 'POW.AF4.BetaL', 'POW.AF4.BetaH']]
# print(df1)
# print(df1["POW.AF3.Theta"])

for ch in chan:
	if ch == "POW.AF4.BetaH":
		fout_data.write(ch)
	else:
		fout_data.write(ch + ",")
fout_data.write("\n")

while i < (len(df1)):
	length = 0
	#	print("i", i)
	#	print("\n")
	for j in range(i, len(df1)):
		#		print("j", j
		#		print("\n")
		if df1.loc[i, "Timestamp"] == df1.loc[j, "Timestamp"]:
			length = length + 1
			time.append(df1.loc[j, "Timestamp"])
			af3_theta.append(df1.loc[j, "POW.AF3.Theta"])
			#			print(type(af3_theta))
			af3_alpha.append(df1.loc[j, "POW.AF3.Alpha"])
			af3_betal.append(df1.loc[j, "POW.AF3.BetaL"])
			af3_betah.append(df1.loc[j, "POW.AF3.BetaH"])
			af4_theta.append(df1.loc[j, "POW.AF4.Theta"])
			af4_alpha.append(df1.loc[j, "POW.AF4.Alpha"])
			af4_betal.append(df1.loc[j, "POW.AF4.BetaL"])
			af4_betah.append(df1.loc[j, "POW.AF4.BetaH"])
		else:
			break
	count = count + 1
	time_m = statistics.mean(time)
	af3_theta_m = statistics.mean(af3_theta)
	af3_alpha_m = statistics.mean(af3_alpha)
	af3_betal_m = statistics.mean(af3_betal)
	af3_betah_m = statistics.mean(af3_betah)
	af4_theta_m = statistics.mean(af4_theta)
	af4_alpha_m = statistics.mean(af4_alpha)
	af4_betal_m = statistics.mean(af4_betal)
	af4_betah_m = statistics.mean(af4_betah)

	del time[:]
	del af3_theta[:]
	del af3_alpha[:]
	del af3_betal[:]
	del af3_betah[:]
	del af4_theta[:]
	del af4_alpha[:]
	del af4_betal[:]
	del af4_betah[:]

	fout_data.write(str(time_m) + ",")
	fout_data.write(str(af3_theta_m) + ",")
	fout_data.write(str(af3_alpha_m) + ",")
	fout_data.write(str(af3_betal_m) + ",")
	fout_data.write(str(af3_betah_m) + ",")

	fout_data.write(str(af4_theta_m) + ",")
	fout_data.write(str(af4_alpha_m) + ",")
	fout_data.write(str(af4_betal_m) + ",")
	fout_data.write(str(af4_betah_m))
	fout_data.write("\n")

	i = i + length
	print(count)
fout_data.close()






#-------------------------------------------------- FOR ALPHA CALIBRATION ------------------------------------------------------------


fout_data = open(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/processed_data/p1_vid_3_20.11.19_18.05.04.bp_processed.csv",
	'w')    #------------------------------------------ CHANGE PATH HERE - Participant ALPHA CALIBRATION, also add processed after the name------------------------------------------
chan = ['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta',
		'POW.AF4.Alpha', 'POW.AF4.BetaL', 'POW.AF4.BetaH']
time, af3_theta, af3_alpha, af3_betal, af3_betah, af4_theta, af4_alpha, af4_betal, af4_betah = ([] for i in range(9))
length = 0
count = 0
i = 0

df = pd.read_csv(
	"/Users/sarvi/PycharmProjects/BCI/Project/datasets/p1/copy_of_original_data/p1_vid_3_20.11.19_18.05.04.bp.csv",
	header=0)  #------------------------------------------ CHANGE PATH HERE - Participant ALPHA CALIBRATION ------------------------------------------
# print(df)

df1 = df[
	['Timestamp', 'POW.AF3.Theta', 'POW.AF3.Alpha', 'POW.AF3.BetaL', 'POW.AF3.BetaH', 'POW.AF4.Theta', 'POW.AF4.Alpha',
	 'POW.AF4.BetaL', 'POW.AF4.BetaH']]
# print(df1)
# print(df1["POW.AF3.Theta"])

for ch in chan:
	if ch == "POW.AF4.BetaH":
		fout_data.write(ch)
	else:
		fout_data.write(ch + ",")
fout_data.write("\n")

while i < (len(df1)):
	length = 0
	#	print("i", i)
	#	print("\n")
	for j in range(i, len(df1)):
		#		print("j", j
		#		print("\n")
		if df1.loc[i, "Timestamp"] == df1.loc[j, "Timestamp"]:
			length = length + 1
			time.append(df1.loc[j, "Timestamp"])
			af3_theta.append(df1.loc[j, "POW.AF3.Theta"])
			#			print(type(af3_theta))
			af3_alpha.append(df1.loc[j, "POW.AF3.Alpha"])
			af3_betal.append(df1.loc[j, "POW.AF3.BetaL"])
			af3_betah.append(df1.loc[j, "POW.AF3.BetaH"])
			af4_theta.append(df1.loc[j, "POW.AF4.Theta"])
			af4_alpha.append(df1.loc[j, "POW.AF4.Alpha"])
			af4_betal.append(df1.loc[j, "POW.AF4.BetaL"])
			af4_betah.append(df1.loc[j, "POW.AF4.BetaH"])
		else:
			break
	count = count + 1
	time_m = statistics.mean(time)
	af3_theta_m = statistics.mean(af3_theta)
	af3_alpha_m = statistics.mean(af3_alpha)
	af3_betal_m = statistics.mean(af3_betal)
	af3_betah_m = statistics.mean(af3_betah)
	af4_theta_m = statistics.mean(af4_theta)
	af4_alpha_m = statistics.mean(af4_alpha)
	af4_betal_m = statistics.mean(af4_betal)
	af4_betah_m = statistics.mean(af4_betah)

	del time[:]
	del af3_theta[:]
	del af3_alpha[:]
	del af3_betal[:]
	del af3_betah[:]
	del af4_theta[:]
	del af4_alpha[:]
	del af4_betal[:]
	del af4_betah[:]

	fout_data.write(str(time_m) + ",")
	fout_data.write(str(af3_theta_m) + ",")
	fout_data.write(str(af3_alpha_m) + ",")
	fout_data.write(str(af3_betal_m) + ",")
	fout_data.write(str(af3_betah_m) + ",")

	fout_data.write(str(af4_theta_m) + ",")
	fout_data.write(str(af4_alpha_m) + ",")
	fout_data.write(str(af4_betal_m) + ",")
	fout_data.write(str(af4_betah_m))
	fout_data.write("\n")

	i = i + length
	print(count)
fout_data.close()













  











