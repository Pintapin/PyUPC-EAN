'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2013 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2013 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2013 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: validate.py - Last Update: 08/03/2013 Ver. 2.4.3 RC 1  - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import sys, re;

def get_digital_root(number):
 while(len(str(number))>1):
  subnum = list(str(number));
  PreCount = 0;
  number = 0;
  while (PreCount<=len(subnum)-1):
   number += int(subnum[PreCount]);
   PreCount += 1;
 return number;
def validate_upca(upc,return_check=False): 
 upc = str(upc);
 if(len(upc)>12):
  fix_matches = re.findall("^(\d{12})", upc);
  upc = fix_matches[0];
 if(len(upc)>12 or len(upc)<11):
  return False;
 if(len(upc)==11):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==12):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches=upc_matches[0];
 OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]+"+"+upc_matches[8]+"+"+upc_matches[10]) * 3;
 EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]+"+"+upc_matches[7]+"+"+upc_matches[9]);
 AllSum = OddSum + EvenSum;
 CheckSum = AllSum % 10;
 if(CheckSum>0):
  CheckSum = 10 - CheckSum;
 if(return_check==False and len(upc)==12):
  if(CheckSum!=int(upc_matches[11])):
   return False;
  if(CheckSum==int(upc_matches[11])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==11):
  return str(CheckSum);
def get_upca_checksum(upc):
 upc = str(upc);
 return validate_upca(upc,True);
def fix_upca_checksum(upc):
 upc = str(upc);
 if(len(upc)>11):
  fix_matches = re.findall("^(\d{11})", upc); 
  upc = fix_matches[0];
 return upc+str(get_upca_checksum(upc));

def validate_ean13(upc,return_check=False):
 upc = str(upc);
 if(len(upc)>13):
  fix_matches = re.findall("^(\d{13})", upc);
  upc = fix_matches[0];
 if(len(upc)>13 or len(upc)<12):
  return False;
 if(len(upc)==12):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==13):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches=upc_matches[0];
 EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]+"+"+upc_matches[7]+"+"+upc_matches[9]+"+"+upc_matches[11]) * 3;
 OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]+"+"+upc_matches[8]+"+"+upc_matches[10]);
 AllSum = OddSum + EvenSum;
 CheckSum = AllSum % 10;
 if(CheckSum>0):
  CheckSum = 10 - CheckSum;
 if(return_check==False and len(upc)==13):
  if(CheckSum!=int(upc_matches[12])):
   return False;
  if(CheckSum==int(upc_matches[12])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==12):
  return str(CheckSum);
def get_ean13_checksum(upc):
 upc = str(upc);
 return validate_ean13(upc,True);
def fix_ean13_checksum(upc):
 upc = str(upc);
 if(len(upc)>12):
  fix_matches = re.findall("^(\d{12})", upc); 
  upc = fix_matches[0];
 return upc+str(get_ean13_checksum(upc));

def validate_itf14(upc,return_check=False):
 upc = str(upc);
 if(len(upc)>14):
  fix_matches = re.findall("^(\d{14})", upc); 
  upc = fix_matches[0];
 if(len(upc)>14 or len(upc)<13):
  return False;
 if(len(upc)==13):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==14):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches=upc_matches[0];
 EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]+"+"+upc_matches[7]+"+"+upc_matches[9]+"+"+upc_matches[11]);
 OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]+"+"+upc_matches[8]+"+"+upc_matches[10]+"+"+upc_matches[12]) * 3;
 AllSum = OddSum + EvenSum;
 CheckSum = AllSum % 10;
 if(CheckSum>0):
  CheckSum = 10 - CheckSum;
 if(return_check==False and len(upc)==14):
  if(CheckSum!=int(upc_matches[13])):
   return False;
  if(CheckSum==int(upc_matches[13])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==13):
  return str(CheckSum);
def get_itf14_checksum(upc):
 upc = str(upc);
 return validate_itf14(upc,True);
def fix_itf14_checksum(upc):
 upc = str(upc);
 if(len(upc)>13):
  fix_matches = re.findall("^(\d{13})", upc); 
  upc = fix_matches[0];
 return upc+str(get_itf14_checksum(upc));

def validate_ean8(upc,return_check=False):
 upc = str(upc);
 if(len(upc)>8):
  fix_matches = re.findall("^(\d{8})", upc); 
  upc = fix_matches[0];
 if(len(upc)>8 or len(upc)<7):
  return False;
 if(len(upc)==7):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==8):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches=upc_matches[0];
 EvenSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
 OddSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
 AllSum = OddSum + EvenSum;
 CheckSum = AllSum % 10;
 if(CheckSum>0):
  CheckSum = 10 - CheckSum;
 if(return_check==False and len(upc)==8):
  if(CheckSum!=int(upc_matches[7])):
   return False;
  if(CheckSum==int(upc_matches[7])): 
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==7):
  return str(CheckSum);
def get_ean8_checksum(upc):
 upc = str(upc);
 return validate_ean8(upc,True);
def fix_ean8_checksum(upc):
 upc = str(upc);
 if(len(upc)>7):
  fix_matches = re.findall("^(\d{7})", upc); 
  upc = fix_matches[0];
 return upc+str(get_ean8_checksum(upc));

def validate_upce(upc,return_check=False):
 upc = str(upc);
 if(len(upc)>8):
  fix_matches = re.findall("/^(\d{8})/", upc); 
  upc = fix_matches[0];
 if(len(upc)>8 or len(upc)<7):
  return False;
 if(not re.findall("^(0|1)", upc)):
  return False;
 CheckDigit = None;
 if(len(upc)==8 and re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc)):
  upc_matches = re.findall("^(\d{7})(\d{1})", upc);
  upc_matches=upc_matches[0];
  CheckDigit = upc_matches[1];
 if(re.findall("^(\d{1})(\d{5})([0-3])", upc)):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
  upc_matches=upc_matches[0];
  if(int(upc_matches[6])==0):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[3]+"+"+upc_matches[5]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[4]);
  if(int(upc_matches[6])==1):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[3]+"+"+upc_matches[5]) * 3;
   EvenSum = eval(upc_matches[1]+"+1+"+upc_matches[4]);
  if(int(upc_matches[6])==2):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[3]+"+"+upc_matches[5]) * 3;
   EvenSum = eval(upc_matches[1]+"+2+"+upc_matches[4]);
  if(int(upc_matches[6])==3):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[5]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[4]);
 if(re.findall("^(\d{1})(\d{5})([4-9])", upc)):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
  upc_matches=upc_matches[0];
  if(int(upc_matches[6])==4):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[5]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]);
  if(int(upc_matches[6])==5):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
  if(int(upc_matches[6])==6):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
  if(int(upc_matches[6])==7):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
  if(int(upc_matches[6])==8):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
  if(int(upc_matches[6])==9):
   OddSum = eval(upc_matches[0]+"+"+upc_matches[2]+"+"+upc_matches[4]+"+"+upc_matches[6]) * 3;
   EvenSum = eval(upc_matches[1]+"+"+upc_matches[3]+"+"+upc_matches[5]);
 AllSum = OddSum + EvenSum;
 CheckSum = AllSum % 10;
 if(CheckSum>0):
  CheckSum = 10 - CheckSum;
 if(return_check==False and len(upc)==8):
  if(CheckSum!=int(CheckDigit)):
   return False;
  if(CheckSum==int(CheckDigit)):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==7):
  return str(CheckSum);
def get_upce_checksum(upc):
 upc = str(upc);
 return validate_upce(upc,True);
def fix_upce_checksum(upc):
 upc = str(upc);
 if(len(upc)>7):
  fix_matches = re.findall("^(\d{7})", upc); 
  upc = fix_matches[0];
 return upc+str(get_upce_checksum(upc));

def validate_ean2(upc,return_check=False): 
 upc = str(upc);
 if(len(upc)>3):
  fix_matches = re.findall("^(\d{3})", upc);
  upc = fix_matches[0];
 if(len(upc)>3 or len(upc)<2):
  return False;
 if(len(upc)==2):
  upc_matches = re.findall("^(\d{2})", upc);
 if(len(upc)==3):
  upc_matches = re.findall("^(\d{2})(\d{1})", upc);
  upc_matches=upc_matches[0];
 if(len(upc_matches)<=0): 
  return False;
 CheckSum = int(upc_matches[0]) % 4;
 if(return_check==False and len(upc)==3):
  if(CheckSum!=int(upc_matches[1])):
   return False;
  if(CheckSum==int(upc_matches[1])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==2):
  return str(CheckSum);
def get_ean2_checksum(upc):
 upc = str(upc);
 return validate_ean2(upc,True);
def fix_ean2_checksum(upc):
 upc = str(upc);
 if(len(upc)>2):
  fix_matches = re.findall("^(\d{2})", upc); 
  upc = fix_matches[0];
 return upc+str(get_ean2_checksum(upc));

def validate_ean5(upc,return_check=False): 
 upc = str(upc);
 if(len(upc)>6):
  fix_matches = re.findall("^(\d{6})", upc);
  upc = fix_matches[0];
 if(len(upc)>6 or len(upc)<5):
  return False;
 if(len(upc)==5):
  upc_matches = re.findall("^(\d{5})", upc);
 if(len(upc)==6):
  upc_matches = re.findall("^(\d{5})(\d{1})", upc);
  upc_matches=upc_matches[0];
 if(len(upc_matches)<=0): 
  return False;
 LeftDigit = list(upc_matches[0]);
 CheckSum = (int(LeftDigit[0]) * 3) + (int(LeftDigit[1]) * 9) + (int(LeftDigit[2]) * 3) + (int(LeftDigit[3]) * 9) + (int(LeftDigit[4]) * 3);
 CheckSum = CheckSum % 10;
 if(return_check==False and len(upc)==6):
  if(CheckSum!=int(upc_matches[1])):
   return False;
  if(CheckSum==int(upc_matches[1])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==5):
  return str(CheckSum);
def get_ean5_checksum(upc):
 upc = str(upc);
 return validate_ean5(upc,True);
def fix_ean5_checksum(upc):
 upc = str(upc);
 if(len(upc)>5):
  fix_matches = re.findall("^(\d{5})", upc); 
  upc = fix_matches[0];
 return upc+str(get_ean5_checksum(upc));

'''
Shortcut Codes by Kazuki Przyborowski
'''
def validate_barcode(upc,return_check=False):
 upc = str(upc);
 if(len(upc)==3): 
  return validate_ean2(upc,return_check);
 if(len(upc)==6): 
  return validate_ean5(upc,return_check);
 if(len(upc)==8): 
  if(re.findall("^([0-1])", upc)):
   return validate_upce(upc,return_check);
  if(re.findall("^([2-9])", upc)):
   return validate_ean8(upc,return_check);
 if(len(upc)==12): 
  return validate_upca(upc,return_check);
 if(len(upc)==13): 
  return validate_ean13(upc,return_check);
 if(len(upc)==14): 
  return validate_itf14(upc,return_check);
 return False;
def get_barcode_checksum(upc):
 upc = str(upc);
 if(len(upc)==2): 
  return validate_ean2(upc,True);
 if(len(upc)==5): 
  return validate_ean5(upc,True);
 if(len(upc)==7): 
  if(re.findall("^([0-1])", upc)):
   return validate_upce(upc,True);
  if(re.findall("^([2-9])", upc)):
   return validate_ean8(upc,True);
 if(len(upc)==11): 
  return validate_upca(upc,True);
 if(len(upc)==12): 
  return validate_ean13(upc,True);
 if(len(upc)==13): 
  return validate_itf14(upc,True);
 return False;
def fix_barcode_checksum(upc):
 upc = str(upc);
 if(len(upc)==3): 
  return upc+str(validate_ean2(upc,True));
 if(len(upc)==6): 
  return upc+str(validate_ean5(upc,True));
 if(len(upc)==7): 
  if(re.findall("^([0-1])", upc)):
   return upc+str(validate_upce(upc,True));
  if(re.findall("^([2-9])", upc)):
   return upc+str(validate_ean8(upc,True));
 if(len(upc)==11): 
  return upc+str(validate_upca(upc,True));
 if(len(upc)==12): 
  return upc+str(validate_ean13(upc,True));
 if(len(upc)==13): 
  return upc+str(validate_itf14(upc,True));
 return False;

def validate_any(upc,return_check=False):
 upc = str(upc);
 if(len(upc)==3): 
  return validate_ean2(upc,return_check);
 if(len(upc)==6): 
  return validate_ean5(upc,return_check);
 if(len(upc)==8): 
  if(re.findall("^([0-1])", upc)):
   return validate_upce(upc,return_check);
  if(re.findall("^([2-9])", upc)):
   return validate_ean8(upc,return_check);
 if(len(upc)==12): 
  return validate_upca(upc,return_check);
 if(len(upc)==13): 
  return validate_ean13(upc,return_check);
 if(len(upc)==14): 
  return validate_itf14(upc,return_check);
 return False;
def get_any_checksum(upc):
 upc = str(upc);
 if(len(upc)==2): 
  return validate_ean2(upc,True);
 if(len(upc)==5): 
  return validate_ean5(upc,True);
 if(len(upc)==7): 
  if(re.findall("^([0-1])", upc)):
   return validate_upce(upc,True);
  if(re.findall("^([2-9])", upc)):
   return validate_ean8(upc,True);
 if(len(upc)==11): 
  return validate_upca(upc,True);
 if(len(upc)==12): 
  return validate_ean13(upc,True);
 if(len(upc)==13): 
  return validate_itf14(upc,True);
 return False;
def fix_any_checksum(upc):
 upc = str(upc);
 if(len(upc)==3): 
  return upc+str(validate_ean2(upc,True));
 if(len(upc)==6): 
  return upc+str(validate_ean5(upc,True));
 if(len(upc)==7): 
  if(re.findall("^([0-1])", upc)):
   return upc+str(validate_upce(upc,True));
  if(re.findall("^([2-9])", upc)):
   return upc+str(validate_ean8(upc,True));
 if(len(upc)==11): 
  return upc+str(validate_upca(upc,True));
 if(len(upc)==12): 
  return upc+str(validate_ean13(upc,True));
 if(len(upc)==13): 
  return upc+str(validate_itf14(upc,True));
 return False;

def validate_upc(upc,return_check=False):
 upc = str(upc);
 if(len(upc)==7 or len(upc)==8): 
  return validate_upce(upc,return_check);
 if(len(upc)==11 or len(upc)==12): 
  return validate_upca(upc,return_check);
 if(len(upc)==13 or len(upc)==14): 
  return validate_itf14(upc,return_check);
 return False;
def get_upc_checksum(upc):
 upc = str(upc);
 if(len(upc)==7 or len(upc)==8): 
  return validate_upce(upc,True);
 if(len(upc)==11 or len(upc)==12): 
  return validate_upca(upc,True);
 if(len(upc)==13 or len(upc)==14): 
  return validate_itf14(upc,True);
 return False;
def fix_upc_checksum(upc):
 upc = str(upc);
 if(len(upc)==7 or len(upc)==8): 
  return upc+str(validate_upce(upc,True));
 if(len(upc)==11 or len(upc)==12): 
  return upc+str(validate_upca(upc,True));
 if(len(upc)==13 or len(upc)==14): 
  return upc+str(validate_itf14(upc,True));
 return False;

def validate_ean(upc,return_check=False):
 upc = str(upc);
 if(len(upc)==3 or len(upc)==3): 
  return validate_ean2(upc,return_check);
 if(len(upc)==6 or len(upc)==6): 
  return validate_ean5(upc,return_check);
 if(len(upc)==8 or len(upc)==8): 
  return validate_ean8(upc,return_check);
 if(len(upc)==13 or len(upc)==13): 
  return validate_ean13(upc,return_check);
 return False;
def get_any_checksum(upc):
 upc = str(upc);
 if(len(upc)==2 or len(upc)==3): 
  return validate_ean2(upc,True);
 if(len(upc)==5 or len(upc)==6): 
  return validate_ean5(upc,True);
 if(len(upc)==7 or len(upc)==8): 
  return validate_ean8(upc,True);
 if(len(upc)==12 or len(upc)==13): 
  return validate_ean13(upc,True);
 return False;
def fix_ean_checksum(upc):
 upc = str(upc);
 if(len(upc)==2 or len(upc)==3): 
  return upc+str(validate_ean2(upc,True));
 if(len(upc)==5 or len(upc)==6): 
  return upc+str(validate_ean5(upc,True));
 if(len(upc)==7 or len(upc)==8): 
  return upc+str(validate_ean8(upc,True));
 if(len(upc)==12 or len(upc)==13): 
  return upc+str(validate_ean13(upc,True));
 return False;

'''
IMEI (International Mobile Station Equipment Identity)
http://en.wikipedia.org/wiki/IMEI#Check_digit_computation
'''
def validate_imei(upc,return_check=False): 
 upc = str(upc);
 if(len(upc)>15):
  fix_matches = re.findall("^(\d{15})", upc);
  upc = fix_matches[0];
 if(len(upc)>15 or len(upc)<14):
  return False;
 upc_matches = list(upc);
 PreChck1 = upc_matches[0:][::2];
 PreChck2 = upc_matches[1:][::2];
 UPC_Sum = int(PreChck1[0]) + get_digital_root(int(PreChck2[0]) * 2) + int(PreChck1[1]) + get_digital_root(int(PreChck2[1]) * 2) + int(PreChck1[2]) + get_digital_root(int(PreChck2[2]) * 2) + int(PreChck1[3]) + get_digital_root(int(PreChck2[3]) * 2) + int(PreChck1[4]) + get_digital_root(int(PreChck2[4]) * 2) + int(PreChck1[5]) + get_digital_root(int(PreChck2[5]) * 2) + int(PreChck1[6]) + get_digital_root(int(PreChck2[6]) * 2);
 PreCheckSum = 0;
 while((UPC_Sum + PreCheckSum) % 10 != 0):
  PreCheckSum += 1;
 CheckSum = PreCheckSum;
 if(return_check==False and len(upc)==15):
  if(CheckSum!=int(PreChck1[7])):
   return False;
  if(CheckSum==int(PreChck1[7])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==14):
  return str(CheckSum);
def get_imei_checksum(upc):
 upc = str(upc);
 return validate_imei(upc,True);
def fix_imei_checksum(upc):
 upc = str(upc);
 if(len(upc)>14):
  fix_matches = re.findall("^(\d{14})", upc); 
  upc = fix_matches[0];
 return upc+str(get_imei_checksum(upc));

'''
Code 11
http://www.barcodeisland.com/code11.phtml
https://en.wikipedia.org/wiki/Code_11
'''
def get_code11_checksum(upc):
 if(len(upc) < 1): 
  return False;
 if(not re.findall("([0-9\-]+)", upc)):
  return False;
 upc = upc.upper();
 upc_matches = list(upc);
 if(len(upc_matches)<=0):
  return False;
 Code11Array = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "-"};
 Code11Values = dict(zip(Code11Array.values(),Code11Array));
 upc_reverse = list(upc_matches);
 upc_reverse.reverse();
 upc_print = list(upc_matches);
 UPC_Count = 0; 
 UPC_Weight = 1; 
 UPC_Sum = 0;
 while (UPC_Count < len(upc_reverse)):
  if(UPC_Weight>10):
   UPC_Weight = 1;
  UPC_Sum = UPC_Sum + (UPC_Weight * Code11Values[str(upc_reverse[UPC_Count])]);
  UPC_Count += 1; 
  UPC_Weight += 1;
 CheckSum = str(Code11Array[UPC_Sum % 11]);
 upc_reverse = list(upc_matches);
 upc_reverse.reverse();
 UPC_Count = 0; 
 UPC_Weight = 1; 
 UPC_Sum = 0;
 while (UPC_Count < len(upc_reverse)):
  if(UPC_Weight>9):
   UPC_Weight = 1;
  UPC_Sum = UPC_Sum + (UPC_Weight * Code11Values[str(upc_reverse[UPC_Count])]);
  UPC_Count += 1; 
  UPC_Weight += 1;
 CheckSum = str(CheckSum)+str(Code11Array[UPC_Sum % 11]);
 return str(CheckSum);

'''
Code 93
http://www.barcodeisland.com/code93.phtml
https://en.wikipedia.org/wiki/Code_93
'''
def get_code93_checksum(upc):
 if(len(upc) < 1): 
  return False;
 if(not re.findall("([0-9a-zA-Z\-\.\$\/\+% ]+)", upc)):
  return False;
 upc = upc.upper();
 upc_matches = list(upc);
 if(len(upc_matches)<=0):
  return False;
 Code93Array = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z", 36: "-", 37: ".", 38: " ", 39: "$", 40: "/", 41: "+", 42: "%", 43: "($)", 44: "(%)", 45: "(/)", 46: "(+)"};
 Code93Values = dict(zip(Code93Array.values(),Code93Array));
 upc_reverse = list(upc_matches);
 upc_reverse.reverse();
 upc_print = list(upc_matches);
 UPC_Count = 0; 
 UPC_Weight = 1; 
 UPC_Sum = 0;
 while (UPC_Count < len(upc_reverse)):
  if(UPC_Weight>20):
   UPC_Weight = 1;
  UPC_Sum = UPC_Sum + (UPC_Weight * Code93Values[str(upc_reverse[UPC_Count])]);
  UPC_Count += 1; 
  UPC_Weight += 1;
 CheckSum = str(Code93Array[UPC_Sum % 47]);
 upc_reverse = list(upc_matches);
 upc_reverse.reverse();
 UPC_Count = 0; 
 UPC_Weight = 1; 
 UPC_Sum = 0;
 while (UPC_Count < len(upc_reverse)):
  if(UPC_Weight>15):
   UPC_Weight = 1;
  UPC_Sum = UPC_Sum + (UPC_Weight * Code93Values[str(upc_reverse[UPC_Count])]);
  UPC_Count += 1; 
  UPC_Weight += 1;
 CheckSum = str(CheckSum)+str(Code93Array[UPC_Sum % 47]);
 return str(CheckSum);

'''
MSI (Modified Plessey)
http://www.barcodeisland.com/msi.phtml
https://en.wikipedia.org/wiki/MSI_Barcode
'''
def get_msi_checksum(upc):
 upc_matches = list(upc);
 if(len(upc) % 2==0):
  PreChck1 = list(str(int("".join(upc_matches[1:][::2])) * 2));
  PreChck2 = upc_matches[0:][::2];
 else:
  PreChck1 = list(str(int("".join(upc_matches[0:][::2])) * 2));
  PreChck2 = upc_matches[1:][::2];
 PreCount = 0;
 UPC_Sum = 0;
 while (PreCount<=len(PreChck1)-1):
  UPC_Sum = UPC_Sum + int(PreChck1[PreCount]);
  PreCount += 1;
 PreCount = 0;
 while (PreCount<=len(PreChck2)-1):
  UPC_Sum = UPC_Sum + int(PreChck2[PreCount]);
  PreCount += 1;
 CheckSum = 10 - (UPC_Sum % 10);
 return str(CheckSum);

'''
ISSN (International Standard Serial Number)
http://en.wikipedia.org/wiki/International_Standard_Serial_Number
'''
def validate_issn8(upc,return_check=False):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>8):
  fix_matches = re.findall("^(\d{8})", upc); 
  fix_matches = fix_matches[0];
  upc = fix_matches[0]+fix_matches[1];
 if(len(upc)>8 or len(upc)<7):
  return False;
 if(len(upc)==7):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==8):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches = upc_matches[0];
 AllSum = eval(upc_matches[0]+"*8") + eval(upc_matches[1]+"*7") + eval(upc_matches[2]+"*6") + eval(upc_matches[3]+"*5") + eval(upc_matches[4]+"*4") + eval(upc_matches[5]+"*3") + eval(upc_matches[6]+"*2");
 CheckSum = AllSum % 11;
 if(CheckSum>0):
  CheckSum = 11 - CheckSum;
 if(return_check==False and len(upc)==8):
  if(CheckSum!=int(upc_matches[7])):
   return False;
  if(CheckSum==int(upc_matches[7])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==7):
  return str(CheckSum);
def get_issn8_checksum(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 return validate_issn8(upc,True);
def fix_issn8_checksum(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>7):
  fix_matches = re.findall("^(\d{7})", upc); 
  upc = fix_matches[0];
 return upc+str(get_issn8_checksum(upc,True));
def validate_issn13(upc,return_check=False):
 upc = str(upc);
 if(not re.findall("^977(\d{9})", upc)):
  return False;
 if(re.findall("^977(\d{9})", upc)):
  return validate_ean13(upc,return_check);
def get_issn13_checksum(upc):
 upc = str(upc);
 return validate_issn13(upc,True);
def fix_issn13_checksum(upc):
 upc = str(upc);
 if(not re.findall("^977(\d{9})", upc)):
  return False;
 if(re.findall("^977(\d{9})", upc)):
  return fix_ean13_checksum(upc);

'''
ISBN (International Standard Book Number)
http://en.wikipedia.org/wiki/ISBN
'''
def validate_isbn10(upc,return_check=False):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>10):
  fix_matches = re.findall("^(\d{9})(\d{1}|X{1})", upc); 
  fix_matches = fix_matches[0];
  upc = fix_matches[0]+fix_matches[1];
 if(len(upc)>10 or len(upc)<9):
  return False;
 if(len(upc)==9):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==10):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1}|X{1})", upc);
 upc_matches = upc_matches[0];
 AllSum = eval(upc_matches[0]+"*10") + eval(upc_matches[1]+"*9") + eval(upc_matches[2]+"*8") + eval(upc_matches[3]+"*7") + eval(upc_matches[4]+"*6") + eval(upc_matches[5]+"*5") + eval(upc_matches[6]+"*4") + eval(upc_matches[7]+"*3") + eval(upc_matches[8]+"*2");
 CheckSum = 0;
 while((AllSum + (CheckSum * 1)) % 11):
  CheckSum += 1;
 if(CheckSum==10):
  CheckSum = "X";
 if(return_check==False and len(upc)==10):
  if(str(CheckSum)!=upc_matches[9]):
   return False;
  if(str(CheckSum)==upc_matches[9]):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==9):
  return str(CheckSum);
def get_isbn10_checksum(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 return validate_isbn10(upc,True);
def fix_isbn10_checksum(upc):
 upc = str(upc);
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>9):
  fix_matches = re.findall("^(\d{9})", upc);
  upc = fix_matches[1];
 return upc+str(get_isbn10_checksum(upc));
def validate_isbn13(upc,return_check=False):
 upc = str(upc);
 if(not re.findall("^978(\d{9})", upc)):
  return False;
 if(re.findall("^978(\d{9})", upc)):
  return validate_ean13(upc,return_check);
def get_isbn13_checksum(upc):
 upc = str(upc);
 return validate_isbn13(upc,True);
def fix_isbn13_checksum(upc):
 upc = str(upc);
 if(not re.findall("^978(\d{9})", upc)):
  return False;
 if(re.findall("^978(\d{9})", upc)):
  return fix_ean13_checksum(upc);

'''
ISMN (International Standard Music Number)
http://en.wikipedia.org/wiki/International_Standard_Music_Number
http://www.ismn-international.org/whatis.html
http://www.ismn-international.org/manual_1998/chapter2.html
'''
def validate_ismn10(upc,return_check=False):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>9):
  fix_matches = re.findall("^(\d{8})(\d{1})", upc); 
  fix_matches = fix_matches[0];
  upc = fix_matches[0]+fix_matches[1];
 if(len(upc)>9 or len(upc)<8):
  return False;
 if(len(upc)==8):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 if(len(upc)==9):
  upc_matches = re.findall("^(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})(\d{1})", upc);
 upc_matches = upc_matches[0];
 AllSum = (3 * 3) + eval(upc_matches[0]+"*1") + eval(upc_matches[1]+"*3") + eval(upc_matches[2]+"*1") + eval(upc_matches[3]+"*3") + eval(upc_matches[4]+"*1") + eval(upc_matches[5]+"*3") + eval(upc_matches[6]+"*1") + eval(upc_matches[7]+"*3");
 CheckSum = 1;
 while((AllSum + (CheckSum * 1)) % 10):
  CheckSum += 1;
 if(return_check==False and len(upc)==9):
  if(CheckSum!=int(upc_matches[8])):
   return False;
  if(CheckSum==int(upc_matches[8])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(upc)==8):
  return str(CheckSum);
def get_ismn10_checksum(upc):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 return validate_ismn10(upc,True);
def fix_ismn10_checksum(upc):
 upc = str(upc);
 upc = upc.replace("M", "");
 upc = upc.replace("-", "");
 upc = upc.replace(" ", "");
 if(len(upc)>9):
  fix_matches = re.findall("^(\d{9})", upc); 
  upc = fix_matches[1];
 return upc+str(get_ismn10_checksum(upc));
def validate_ismn13(upc,return_check=False):
 upc = str(upc);
 if(not re.findall("^9790(\d{8})", upc)):
  return False;
 if(re.findall("^9790(\d{8})", upc)):
  return validate_ean13(upc,return_check);
def get_ismn13_checksum(upc):
 upc = str(upc);
 return validate_ismn13(upc,True);
def fix_ismn13_checksum(upc):
 upc = str(upc);
 if(not re.findall("^9790(\d{8})", upc)):
  return False;
 if(re.findall("^9790(\d{8})", upc)):
  return fix_ean13_checksum(upc);

'''
// Get variable weight price checksum
// Source: http://wiki.answers.com/Q/How_does_a_price_embedded_bar_code_work
// Source: http://en.wikipedia.org/wiki/Universal_Product_Code#Prefixes
// Source: http://barcodes.gs1us.org/GS1%20US%20BarCodes%20and%20eCom%20-%20The%20Global%20Language%20of%20Business.htm
'''
def get_vw_price_checksum(price,return_check=False):
 price = str(price);
 if(len(price)==1):
  price = "000".price;
 if(len(price)==2):
  price = "00".price;
 if(len(price)==3):
  price = "0".price;
 if(len(price)>5):
  if(re.findall("^(\d{5})", price)):
   price_matches = re.findall("^(\d{5})", price);
   price = price_matches[0];
 price_split = list(price);
 numrep1 = [0, 2, 4, 6, 8, 9, 1, 3, 5, 7];
 numrep2 = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7];
 numrep3 = [0, 5, 9, 4, 8, 3, 7, 2, 6, 1];
 if(len(price)==4):
  price_split[0] = numrep1[int(price_split[0])];
  price_split[1] = numrep1[int(price_split[1])];
  price_split[2] = numrep2[int(price_split[2])];
  price_split[3] = numrep3[int(price_split[3])];
  price_add = (price_split[0] + price_split[1] + price_split[2] + price_split[3]) * 3;
 if(len(price)==5):
  price_split[1] = numrep1[int(price_split[1])];
  price_split[2] = numrep1[int(price_split[2])];
  price_split[3] = numrep2[int(price_split[3])];
  price_split[4] = numrep3[int(price_split[4])]; 
  price_add = (price_split[1] + price_split[2] + price_split[3] + price_split[4]) * 3;
 CheckSum = price_add % 10;
 if(return_check==False and len(price)==5):
  if(CheckSum!=int(price_split[0])):
   return False;
  if(CheckSum==int(price_split[0])):
   return True;
 if(return_check==True):
  return str(CheckSum);
 if(len(price)==4):
  return str(CheckSum);
 return str(CheckSum);
def fix_vw_price_checksum(price):
 price = str(price);
 if(len(price)==5):
  fix_matches = re.findall("^(\d{1})(\d{4})", price); 
  fix_matches = fix_matches[0];
  price = fix_matches[1];
 if(len(price)>4):
  fix_matches = re.findall("^(\d{4})", price); 
  price = fix_matches[0];
 return str(get_vw_price_checksum(price,True))+price;
