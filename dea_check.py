dea_1 = False
dea_2 = False
dea_cal_1 = 0
dea_cal_2 = 0
dea_tot = 0
dea_check = input("Enter DEA : ")
dealen = len(dea_check)
if dealen == 9 and  dea_check.isalnum():
 dea_1 = dea_check[0:2]
 dea_2 = dea_check[2:]
 if dea_1.isalpha() and dea_2.isnumeric() :
  if dea_1.isupper() :
   dea_cal_1 = int(dea_2[0:1]) + int(dea_2[2:3]) + int(dea_2[4:5])
   dea_cal_2 = (int(dea_2[1:2]) + int(dea_2[3:4]) + int(dea_2[5:6])) * 2
   dea_tot =dea_cal_1 + dea_cal_2
   alfa_dea = (f"{dea_tot}")
   print(f"DEA calculation {alfa_dea}")
   if alfa_dea[-1:] == dea_2[-1:]:
    print("DEA Verified, using calculation")
   else:
     print("DEA verification failed")
  else:
   print("The first two Character must be in upper case")
 else:
  print("DEA number must have 2 alphabet and 7 numbers.\nExample AB2345678")
else:
  print("DEA number must have 2 alphabet and 7 numbers.\nExample AB2345678")