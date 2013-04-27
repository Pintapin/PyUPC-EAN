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

    $FileInfo: ean8.py - Last Update: 04/27/2013 Ver. 2.4.2 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import cairo, re, sys, types, upcean.precairo, upcean.validate, upcean.convert;
import upcean.ean2, upcean.ean5;
from upcean.precairo import *;
from upcean.validate import *;
from upcean.convert import *;
from upcean.ean2 import *;
from upcean.ean5 import *;

def create_ean8(upc,outfile="./ean8.png",resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 upc = str(upc);
 hidesn = hideinfo[0];
 hidecd = hideinfo[1];
 hidetext = hideinfo[2];
 upc_pieces = None; supplement = None;
 if(re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]{1})([0-9]{2})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(re.findall("([0-9]+)([ |\|]){1}([0-9]{5})$", upc)):
  upc_pieces = re.findall("([0-9]+)([ |\|]){1}([0-9]{5})$", upc);
  upc_pieces = upc_pieces[0];
  upc = upc_pieces[0]; supplement = upc_pieces[2];
 if(len(upc)==7):
  upc = upc+validate_ean8(upc,True);
 if(len(upc)>8 or len(upc)<8):
  return False;
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 if(validate_ean8(upc)==False):
  pre_matches = re.findall("^(\d{7})", upc); 
  upc = pre_matches[0]+str(validate_ean8(pre_matches[0],True));
 upc_matches = re.findall("(\d{4})(\d{4})", upc);
 upc_matches = upc_matches[0];
 if(len(upc_matches)<=0):
  return False;
 LeftDigit = list(upc_matches[0]);
 upc_matches_new = re.findall("(\d{2})(\d{2})", upc_matches[0]);
 upc_matches_new= upc_matches_new[0];
 LeftLeftDigit = upc_matches_new[0];
 LeftRightDigit = upc_matches_new[1];
 RightDigit = list(upc_matches[1]);
 upc_matches_new = re.findall("(\d{2})(\d{2})", upc_matches[1]);
 upc_matches_new= upc_matches_new[0];
 RightLeftDigit = upc_matches_new[0];
 RightRightDigit = upc_matches_new[1];
 addonsize = 0;
 if(supplement!=None and len(supplement)==2): 
  addonsize = 29;
 if(supplement!=None and len(supplement)==5): 
  addonsize = 56;
 upc_preimg = cairo.ImageSurface(cairo.FORMAT_RGB24, 83 + addonsize, barheight[1] + 8);
 upc_img = cairo.Context (upc_preimg);
 upc_img.set_antialias(cairo.ANTIALIAS_NONE);
 upc_img.rectangle(0, 0, 83 + addonsize, barheight[1] + 8);
 upc_img.set_source_rgb(barcolor[2][0], barcolor[2][1], barcolor[2][2]);
 upc_img.fill();
 if(hidetext==False):
  drawColorText(upc_img, 10, 10, barheight[1] + 2, LeftLeftDigit, barcolor[1]);
  drawColorText(upc_img, 10, 23, barheight[1] + 2, LeftRightDigit, barcolor[1]);
  drawColorText(upc_img, 10, 42, barheight[1] + 2, RightLeftDigit, barcolor[1]);
  drawColorText(upc_img, 10, 55, barheight[1] + 2, RightRightDigit, barcolor[1]);
 drawColorLine(upc_img, 0, 10, 0, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 1, 10, 1, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 2, 10, 2, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 3, 10, 3, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 4, 10, 4, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 5, 10, 5, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 6, 10, 6, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 7, 10, 7, barheight[1], barcolor[0]);
 drawColorLine(upc_img, 8, 10, 8, barheight[1], barcolor[2]);
 drawColorLine(upc_img, 9, 10, 9, barheight[1], barcolor[0]);
 NumZero = 0; 
 LineStart = 10;
 while (NumZero < len(LeftDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  left_barcolor_l = [0, 0, 0, 0, 0, 0, 0]; 
  left_barcolor_g = [1, 1, 1, 1, 1, 1, 1];
  if(int(LeftDigit[NumZero])==0): 
   left_barcolor_l = [0, 0, 0, 1, 1, 0, 1]; 
   left_barcolor_g = [0, 1, 0, 0, 1, 1, 1];
  if(int(LeftDigit[NumZero])==1): 
   left_barcolor_l = [0, 0, 1, 1, 0, 0, 1]; 
   left_barcolor_g = [0, 1, 1, 0, 0, 1, 1];
  if(int(LeftDigit[NumZero])==2): 
   left_barcolor_l = [0, 0, 1, 0, 0, 1, 1]; 
   left_barcolor_g = [0, 0, 1, 1, 0, 1, 1];
  if(int(LeftDigit[NumZero])==3): 
   left_barcolor_l = [0, 1, 1, 1, 1, 0, 1]; 
   left_barcolor_g = [0, 1, 0, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==4): 
   left_barcolor_l = [0, 1, 0, 0, 0, 1, 1]; 
   left_barcolor_g = [0, 0, 1, 1, 1, 0, 1];
  if(int(LeftDigit[NumZero])==5): 
   left_barcolor_l = [0, 1, 1, 0, 0, 0, 1]; 
   left_barcolor_g = [0, 1, 1, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==6): 
   left_barcolor_l = [0, 1, 0, 1, 1, 1, 1]; 
   left_barcolor_g = [0, 0, 0, 0, 1, 0, 1];
  if(int(LeftDigit[NumZero])==7): 
   left_barcolor_l = [0, 1, 1, 1, 0, 1, 1]; 
   left_barcolor_g = [0, 0, 1, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==8): 
   left_barcolor_l = [0, 1, 1, 0, 1, 1, 1]; 
   left_barcolor_g = [0, 0, 0, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==9):
   left_barcolor_l = [0, 0, 0, 1, 0, 1, 1];
   left_barcolor_g = [0, 0, 1, 0, 1, 1, 1];
  left_barcolor = left_barcolor_l;
  if(int(upc_matches[1])==1):
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==4):
    left_barcolor = left_barcolor_g;
   if(NumZero==5):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==2):
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==3):
    left_barcolor = left_barcolor_g;
   if(NumZero==5):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==3):
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==3):
    left_barcolor = left_barcolor_g;
   if(NumZero==4):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==4):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==4):
    left_barcolor = left_barcolor_g;
   if(NumZero==5):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==5):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==5):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==6):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==3):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==7):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==3):
    left_barcolor = left_barcolor_g;
   if(NumZero==5):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==8):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==3):
    left_barcolor = left_barcolor_g;
   if(NumZero==4):
    left_barcolor = left_barcolor_g;
  if(int(upc_matches[1])==9):
   if(NumZero==1):
    left_barcolor = left_barcolor_g;
   if(NumZero==2):
    left_barcolor = left_barcolor_g;
   if(NumZero==4):
    left_barcolor = left_barcolor_g;
  InnerUPCNum = 0;
  while (InnerUPCNum < len(left_barcolor)):
   if(left_barcolor[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, barcolor[0]);
   if(left_barcolor[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, barcolor[2]);
   LineStart += 1;
   InnerUPCNum += 1;
  NumZero += 1;
 drawColorLine(upc_img, 38, 10, 38, barheight[1], barcolor[2]);
 drawColorLine(upc_img, 39, 10, 39, barheight[1], barcolor[0]);
 drawColorLine(upc_img, 40, 10, 40, barheight[1], barcolor[2]);
 drawColorLine(upc_img, 41, 10, 41, barheight[1], barcolor[0]);
 drawColorLine(upc_img, 42, 10, 42, barheight[1], barcolor[2]);
 NumZero = 0; LineStart = 43;
 while (NumZero < len(RightDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  right_barcolor = [0, 0, 0, 0, 0, 0, 0];
  if(int(RightDigit[NumZero])==0): 
   right_barcolor = [1, 1, 1, 0, 0, 1, 0];
  if(int(RightDigit[NumZero])==1): 
   right_barcolor = [1, 1, 0, 0, 1, 1, 0];
  if(int(RightDigit[NumZero])==2): 
   right_barcolor = [1, 1, 0, 1, 1, 0, 0];
  if(int(RightDigit[NumZero])==3): 
   right_barcolor = [1, 0, 0, 0, 0, 1, 0];
  if(int(RightDigit[NumZero])==4): 
   right_barcolor = [1, 0, 1, 1, 1, 0, 0];
  if(int(RightDigit[NumZero])==5): 
   right_barcolor = [1, 0, 0, 1, 1, 1, 0];
  if(int(RightDigit[NumZero])==6): 
   right_barcolor = [1, 0, 1, 0, 0, 0, 0];
  if(int(RightDigit[NumZero])==7): 
   right_barcolor = [1, 0, 0, 0, 1, 0, 0];
  if(int(RightDigit[NumZero])==8): 
   right_barcolor = [1, 0, 0, 1, 0, 0, 0];
  if(int(RightDigit[NumZero])==9): 
   right_barcolor = [1, 1, 1, 0, 1, 0, 0];
  InnerUPCNum = 0;
  while (InnerUPCNum < len(right_barcolor)):
   if(right_barcolor[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, barcolor[0]);
   if(right_barcolor[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, barcolor[2]);
   LineStart += 1;
   InnerUPCNum += 1;
  NumZero += 1;
 drawColorLine(upc_img, 71, 10, 71, barheight[1], barcolor[0]);
 drawColorLine(upc_img, 72, 10, 72, barheight[1], barcolor[2]);
 drawColorLine(upc_img, 73, 10, 73, barheight[1], barcolor[0]);
 drawColorLine(upc_img, 74, 10, 74, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 75, 10, 75, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 76, 10, 76, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 77, 10, 77, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 78, 10, 78, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 79, 10, 79, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 80, 10, 80, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 81, 10, 81, barheight[0], barcolor[2]);
 drawColorLine(upc_img, 82, 10, 82, barheight[0], barcolor[2]);
 if(supplement!=None and len(supplement)==2):
  upc_sup_img = draw_ean2_supplement(supplement,1,hideinfo,barheight,barcolor);
  upc_img.set_source_surface(upc_sup_img, 83, 0);
  upc_img.paint();
  del(upc_sup_img);
 if(supplement!=None and len(supplement)==5):
  upc_sup_img = draw_ean5_supplement(supplement,1,hideinfo,barheight,barcolor);
  upc_img.set_source_surface(upc_sup_img, 83, 0);
  upc_img.paint();
  del(upc_sup_img);
 upc_imgpat = cairo.SurfacePattern(upc_preimg);
 scaler = cairo.Matrix();
 scaler.scale(1/int(resize),1/int(resize));
 upc_imgpat.set_matrix(scaler);
 upc_imgpat.set_filter(cairo.FILTER_NEAREST);
 new_upc_preimg = cairo.ImageSurface(cairo.FORMAT_RGB24, (83 + addonsize) * int(resize), (barheight[1] + 8) * int(resize));
 new_upc_img = cairo.Context(new_upc_preimg);
 new_upc_img.set_source(upc_imgpat);
 new_upc_img.paint();
 del(upc_preimg);
 if(outfile is None or isinstance(outfile, bool)):
  return new_upc_preimg;
 if(sys.version[0]=="2"):
  if(outfile=="-" or outfile=="" or outfile==" "):
   new_upc_preimg.write_to_png(sys.stdout);
 if(sys.version[0]=="3"):
  if(outfile=="-" or outfile=="" or outfile==" "):
   new_upc_preimg.write_to_png(sys.stdout.buffer);
 if(outfile!="-" and outfile!="" and outfile!=" "):
  new_upc_preimg.write_to_png(outfile);
 return True;

def draw_ean8(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 return create_ean8(upc,None,resize,hideinfo,barheight,barcolor);

def create_ean8_from_list(upc,outfile,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 if(sys.version[0]=="2"):
  if(isinstance(upc, str) or isinstance(upc, unicode)):
   return create_ean8(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(sys.version[0]=="3"):
  if(isinstance(upc, str)):
   return create_ean8(upc,outfile,resize,hideinfo,barheight,barcolor);
 if(isinstance(upc, tuple) or isinstance(upc, list)):
  NumLoop = 0;
  retlist = list();
  while (NumLoop < len(upc)):
   if(isinstance(resize, tuple) or isinstance(resize, list)):
    resize_val = resize[NumLoop];
   if(sys.version[0]=="2"):
    if(isinstance(resize, str) or isinstance(resize, unicode) or isinstance(resize, int)):
     resize_val = resize;
   if(sys.version[0]=="3"):
    if(isinstance(resize, str) or isinstance(resize, int)):
     resize_val = resize;
   if(isinstance(hideinfo[0], tuple) or isinstance(hideinfo[0], list)):
    hideinfo_val = hideinfo[NumLoop];
   if(isinstance(hideinfo[0], bool)):
    hideinfo_val = hideinfo;
   if(isinstance(barheight[0], tuple) or isinstance(barheight[0], list)):
    barheight_val = barheight[NumLoop];
   if(isinstance(barheight[0], int)):
    barheight_val = barheight;
   if(isinstance(barcolor[0][0], tuple) or isinstance(barcolor[0][0], list)):
    barcolor_val = barcolor[NumLoop];
   if(isinstance(barcolor[0][0], int)):
    barcolor_val = barcolor;
   retlist.append(create_ean8(upc[NumLoop],outfile[NumLoop],resize_val,hideinfo_val,barheight_val,barcolor_val));
   NumLoop = NumLoop + 1;
 return retlist;

def draw_ean8_from_list(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54),barcolor=((0, 0, 0), (0, 0, 0), (255, 255, 255))):
 if(sys.version[0]=="2"):
  if(isinstance(upc, str) or isinstance(upc, unicode)):
   return draw_ean8(upc,resize,hideinfo,barheight);
 if(sys.version[0]=="3"):
  if(isinstance(upc, str)):
   return draw_ean8(upc,resize,hideinfo,barheight);
 if(isinstance(upc, tuple) or isinstance(upc, list)):
  NumLoop = 0;
  drawlist = list();
  while (NumLoop < len(upc)):
   if(isinstance(resize, tuple) or isinstance(resize, list)):
    resize_val = resize[NumLoop];
   if(sys.version[0]=="2"):
    if(isinstance(resize, str) or isinstance(resize, unicode) or isinstance(resize, int)):
     resize_val = resize;
   if(sys.version[0]=="3"):
    if(isinstance(resize, str) or isinstance(resize, int)):
     resize_val = resize;
   if(isinstance(hideinfo[0], tuple) or isinstance(hideinfo[0], list)):
    hideinfo_val = hideinfo[NumLoop];
   if(isinstance(hideinfo[0], bool)):
    hideinfo_val = hideinfo;
   if(isinstance(barheight[0], tuple) or isinstance(barheight[0], list)):
    barheight_val = barheight[NumLoop];
   if(isinstance(barheight[0], int)):
    barheight_val = barheight;
   if(isinstance(barcolor[0][0], tuple) or isinstance(barcolor[0][0], list)):
    barcolor_val = barcolor[NumLoop];
   if(isinstance(barcolor[0][0], int)):
    barcolor_val = barcolor;
   drawlist.append(draw_ean8(upc[NumLoop],resize_val,hideinfo_val,barheight_val,barcolor_val));
   NumLoop = NumLoop + 1;
 return drawlist;
