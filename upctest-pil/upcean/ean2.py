#!/usr/bin/python

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

    $FileInfo: ean2.py - Last Update: 04/25/2013 Ver. 2.4.0 RC 1 - Author: cooldude2k $
'''

from __future__ import division, absolute_import, print_function;
import re, os, sys, types, upcean.prepil;
from PIL import Image, ImageDraw, ImageFont;
from upcean.prepil import *;

def create_ean2_supplement(upc,outfile="./ean2_supplement.png",resize=1,hideinfo=(False, False, False),barheight=(47, 53)):
 upc = str(upc);
 hidesn = hideinfo[0];
 hidecd = hideinfo[1];
 hidetext = hideinfo[2];
 if(len(upc)>2 or len(upc)<2): 
  return False;
 upc_matches = re.findall("(\d{2})", upc);
 if(len(upc_matches)<=0): 
  return False;
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 CheckSum = int(upc_matches[0]) % 4;
 LeftDigit = list(upc_matches[0]);
 upc_preimg = Image.new("RGB", (29, barheight[1] + 9));
 upc_img = ImageDraw.Draw(upc_preimg);
 upc_img.rectangle([(0, 0), (29, barheight[1] + 9)], fill=(256, 256, 256));
 text_color = (0, 0, 0);
 alt_text_color = (256, 256, 256);
 LineSize = barheight[0];
 if(hidetext==True):
  LineSize = barheight[1];
 drawColorLine(upc_img, 0, 10, 0, LineSize, alt_text_color);
 drawColorLine(upc_img, 1, 10, 1, LineSize, text_color);
 drawColorLine(upc_img, 2, 10, 2, LineSize, alt_text_color);
 drawColorLine(upc_img, 3, 10, 3, LineSize, text_color);
 drawColorLine(upc_img, 4, 10, 4, LineSize, text_color);
 NumZero = 0; 
 LineStart = 5;
 while (NumZero < len(LeftDigit)):
  LineSize = barheight[0];
  if(hidetext==True):
   LineSize = barheight[1];
  left_text_color_l = [0, 0, 0, 0, 0, 0, 0]; 
  left_text_color_g = [1, 1, 1, 1, 1, 1, 1];
  if(int(LeftDigit[NumZero])==0): 
   left_text_color_l = [0, 0, 0, 1, 1, 0, 1]; 
   left_text_color_g = [0, 1, 0, 0, 1, 1, 1];
  if(int(LeftDigit[NumZero])==1): 
   left_text_color_l = [0, 0, 1, 1, 0, 0, 1]; 
   left_text_color_g = [0, 1, 1, 0, 0, 1, 1];
  if(int(LeftDigit[NumZero])==2): 
   left_text_color_l = [0, 0, 1, 0, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 1, 0, 1, 1];
  if(int(LeftDigit[NumZero])==3): 
   left_text_color_l = [0, 1, 1, 1, 1, 0, 1]; 
   left_text_color_g = [0, 1, 0, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==4): 
   left_text_color_l = [0, 1, 0, 0, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 1, 1, 0, 1];
  if(int(LeftDigit[NumZero])==5): 
   left_text_color_l = [0, 1, 1, 0, 0, 0, 1]; 
   left_text_color_g = [0, 1, 1, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==6): 
   left_text_color_l = [0, 1, 0, 1, 1, 1, 1]; 
   left_text_color_g = [0, 0, 0, 0, 1, 0, 1];
  if(int(LeftDigit[NumZero])==7): 
   left_text_color_l = [0, 1, 1, 1, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 0, 0, 0, 1];
  if(int(LeftDigit[NumZero])==8): 
   left_text_color_l = [0, 1, 1, 0, 1, 1, 1]; 
   left_text_color_g = [0, 0, 0, 1, 0, 0, 1];
  if(int(LeftDigit[NumZero])==9): 
   left_text_color_l = [0, 0, 0, 1, 0, 1, 1]; 
   left_text_color_g = [0, 0, 1, 0, 1, 1, 1];
  left_text_color = left_text_color_l;
  if(CheckSum==0 and NumZero==0): 
   left_text_color = left_text_color_l;
  if(CheckSum==0 and NumZero==1): 
   left_text_color = left_text_color_l;
  if(CheckSum==1 and NumZero==0): 
   left_text_color = left_text_color_l;
  if(CheckSum==1 and NumZero==1): 
   left_text_color = left_text_color_g;
  if(CheckSum==2 and NumZero==0): 
   left_text_color = left_text_color_g;
  if(CheckSum==2 and NumZero==1): 
   left_text_color = left_text_color_l;
  if(CheckSum==3 and NumZero==0): 
   left_text_color = left_text_color_g;
  if(CheckSum==3 and NumZero==1): 
   left_text_color = left_text_color_g;
  InnerUPCNum = 0;
  while (InnerUPCNum < len(left_text_color)):
   if(left_text_color[InnerUPCNum]==1):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, text_color);
   if(left_text_color[InnerUPCNum]==0):
    drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, alt_text_color);
   LineStart += 1;
   InnerUPCNum += 1;
  if(NumZero == 0):
   drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, alt_text_color);
   LineStart += 1;
   drawColorLine(upc_img, LineStart, 10, LineStart, LineSize, text_color);
   LineStart += 1;
  NumZero += 1;
 new_upc_img = upc_preimg.resize((29 * int(resize), (barheight[1] + 9) * int(resize)), Image.NEAREST);
 del(upc_img);
 del(upc_preimg);
 upc_img = ImageDraw.Draw(new_upc_img);
 if(hidetext==False):
  drawColorText(upc_img, 10 * int(resize), 5 + (6 * (int(resize) - 1)), barheight[0] + (barheight[0] * (int(resize) - 1)), LeftDigit[0], text_color);
  drawColorText(upc_img, 10 * int(resize), 13 + (13 * (int(resize) - 1)), barheight[0] + (barheight[0] * (int(resize) - 1)), LeftDigit[1], text_color);
 del(upc_img);
 if(sys.version[0]=="2"):
  if(isinstance(outfile, str) or isinstance(outfile, unicode)):
   oldoutfile = outfile[:];
 if(sys.version[0]=="3"):
  if(isinstance(outfile, str)):
   oldoutfile = outfile[:];
 if(isinstance(outfile, tuple)):
  oldoutfile = tuple(outfile[:]);
 if(isinstance(outfile, list)):
  oldoutfile = list(outfile[:]);
 if(outfile is None or isinstance(outfile, bool)):
  oldoutfile = None;
 if(sys.version[0]=="2"):
  if(isinstance(oldoutfile, str) or isinstance(outfile, unicode)):
   if(outfile!="-" and outfile!="" and outfile!=" "):
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))>0):
     outfileext = re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))>0):
     tmpoutfile = re.findall("(.*)\:([a-zA-Z]+)", oldoutfile);
     del(outfile);
     outfile = tmpoutfile[0][0];
     outfileext = tmpoutfile[0][1].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))==0):
     outfileext = "PNG";
   if(outfileext=="DIB"):
    outfileext = "BMP";
   if(outfileext=="PS"):
    outfileext = "EPS";
   if(outfileext=="JPG" or outfileext=="JPE" or outfileext=="JFIF" or outfileext=="JFI"):
    outfileext = "JPEG";
   if(outfileext=="PBM" or outfileext=="PGM"):
    outfileext = "PPM";
   if(outfileext=="TIF"):
    outfileext = "TIFF";
   if(outfileext!="BMP" and outfileext!="EPS" and outfileext!="GIF" and outfileext!="IM" and outfileext!="JPEG" and outfileext!="PCX" and outfileext!="PDF" and outfileext!="PNG" and outfileext!="PPM" and outfileext!="TIFF" and outfileext!="XPM"):
    outfileext = "PNG";
 if(sys.version[0]=="3"):
  if(isinstance(oldoutfile, str)):
   if(outfile!="-" and outfile!="" and outfile!=" "):
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))>0):
     outfileext = re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))>0):
     tmpoutfile = re.findall("(.*)\:([a-zA-Z]+)", oldoutfile);
     del(outfile);
     outfile = tmpoutfile[0][0];
     outfileext = tmpoutfile[0][1].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))==0):
     outfileext = "PNG";
   if(outfileext=="DIB"):
    outfileext = "BMP";
   if(outfileext=="PS"):
    outfileext = "EPS";
   if(outfileext=="JPG" or outfileext=="JPE" or outfileext=="JFIF" or outfileext=="JFI"):
    outfileext = "JPEG";
   if(outfileext=="PBM" or outfileext=="PGM"):
    outfileext = "PPM";
   if(outfileext=="TIF"):
    outfileext = "TIFF";
   if(outfileext!="BMP" and outfileext!="EPS" and outfileext!="GIF" and outfileext!="IM" and outfileext!="JPEG" and outfileext!="PCX" and outfileext!="PDF" and outfileext!="PNG" and outfileext!="PPM" and outfileext!="TIFF" and outfileext!="XPM"):
    outfileext = "PNG";
 if(isinstance(oldoutfile, tuple) or isinstance(oldoutfile, list)):
  del(outfile);
  outfile = oldoutfile[0];
  outfileext = oldoutfile[1];
 if(outfile is None or isinstance(outfile, bool)):
  return new_upc_img;
 if(sys.version[0]=="2"):
  if(outfile=="-" or outfile=="" or outfile==" " or outfile==None):
   new_upc_img.save(sys.stdout, outfileext);
 if(sys.version[0]=="3"):
  if(outfile=="-" or outfile=="" or outfile==" " or outfile==None):
   new_upc_img.save(sys.stdout.buffer, outfileext);
 if(outfile!="-" and outfile!="" and outfile!=" "):
  new_upc_img.save(outfile, outfileext);
 return True;

def draw_ean2_supplement(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54)):
 return create_ean2_supplement(upc,None,resize,hideinfo,barheight);

def create_ean2(upc,outfile="./ean2.png",resize=1,hideinfo=(False, False, False),barheight=(47, 53)):
 if(not re.findall("^([0-9]*[\.]?[0-9])", str(resize)) or int(resize) < 1):
  resize = 1;
 upc_preimg = Image.new("RGB", ((29 * int(resize)) + (8 * int(resize)), (barheight[1] + 9) * int(resize)));
 upc_img = ImageDraw.Draw(upc_preimg);
 upc_img.rectangle([(0, 0), ((29 * int(resize)) + (8 * int(resize)), (barheight[1] + 9) * int(resize))], fill=(256, 256, 256));
 text_color = (0, 0, 0);
 alt_text_color = (256, 256, 256);
 upc_sup_img = draw_ean2_supplement(upc,resize,hideinfo,barheight);
 if(upc_sup_img is None or isinstance(upc_sup_img, bool)):
  return False;
 upc_preimg.paste(upc_sup_img,(8 * int(resize),0));
 del(upc_sup_img);
 del(upc_img);
 if(sys.version[0]=="2"):
  if(isinstance(outfile, str) or isinstance(outfile, unicode)):
   oldoutfile = outfile[:];
 if(sys.version[0]=="3"):
  if(isinstance(outfile, str)):
   oldoutfile = outfile[:];
 if(isinstance(outfile, tuple)):
  oldoutfile = tuple(outfile[:]);
 if(isinstance(outfile, list)):
  oldoutfile = list(outfile[:]);
 if(outfile is None or isinstance(outfile, bool)):
  oldoutfile = None;
 if(sys.version[0]=="2"):
  if(isinstance(oldoutfile, str) or isinstance(outfile, unicode)):
   if(outfile!="-" and outfile!="" and outfile!=" "):
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))>0):
     outfileext = re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))>0):
     tmpoutfile = re.findall("(.*)\:([a-zA-Z]+)", oldoutfile);
     del(outfile);
     outfile = tmpoutfile[0][0];
     outfileext = tmpoutfile[0][1].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))==0):
     outfileext = "PNG";
   if(outfileext=="DIB"):
    outfileext = "BMP";
   if(outfileext=="PS"):
    outfileext = "EPS";
   if(outfileext=="JPG" or outfileext=="JPE" or outfileext=="JFIF" or outfileext=="JFI"):
    outfileext = "JPEG";
   if(outfileext=="PBM" or outfileext=="PGM"):
    outfileext = "PPM";
   if(outfileext=="TIF"):
    outfileext = "TIFF";
   if(outfileext!="BMP" and outfileext!="EPS" and outfileext!="GIF" and outfileext!="IM" and outfileext!="JPEG" and outfileext!="PCX" and outfileext!="PDF" and outfileext!="PNG" and outfileext!="PPM" and outfileext!="TIFF" and outfileext!="XPM"):
    outfileext = "PNG";
 if(sys.version[0]=="3"):
  if(isinstance(oldoutfile, str)):
   if(outfile!="-" and outfile!="" and outfile!=" "):
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))>0):
     outfileext = re.findall("^\.([A-Za-z]+)", os.path.splitext(outfile)[1])[0].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))>0):
     tmpoutfile = re.findall("(.*)\:([a-zA-Z]+)", oldoutfile);
     del(outfile);
     outfile = tmpoutfile[0][0];
     outfileext = tmpoutfile[0][1].upper();
    if(len(re.findall("^\.([A-Za-z]+)$", os.path.splitext(oldoutfile)[1]))==0 and len(re.findall("(.*)\:([a-zA-Z]+)", oldoutfile))==0):
     outfileext = "PNG";
   if(outfileext=="DIB"):
    outfileext = "BMP";
   if(outfileext=="PS"):
    outfileext = "EPS";
   if(outfileext=="JPG" or outfileext=="JPE" or outfileext=="JFIF" or outfileext=="JFI"):
    outfileext = "JPEG";
   if(outfileext=="PBM" or outfileext=="PGM"):
    outfileext = "PPM";
   if(outfileext=="TIF"):
    outfileext = "TIFF";
   if(outfileext!="BMP" and outfileext!="EPS" and outfileext!="GIF" and outfileext!="IM" and outfileext!="JPEG" and outfileext!="PCX" and outfileext!="PDF" and outfileext!="PNG" and outfileext!="PPM" and outfileext!="TIFF" and outfileext!="XPM"):
    outfileext = "PNG";
 if(isinstance(oldoutfile, tuple) or isinstance(oldoutfile, list)):
  del(outfile);
  outfile = oldoutfile[0];
  outfileext = oldoutfile[1];
 if(outfile is None or isinstance(outfile, bool)):
  return upc_preimg;
 if(sys.version[0]=="2"):
  if(outfile=="-" or outfile=="" or outfile==" " or outfile==None):
   upc_preimg.save(sys.stdout, outfileext);
 if(sys.version[0]=="3"):
  if(outfile=="-" or outfile=="" or outfile==" " or outfile==None):
   upc_preimg.save(sys.stdout.buffer, outfileext);
 if(outfile!="-" and outfile!="" and outfile!=" "):
  upc_preimg.save(outfile, outfileext);
 return True;

def draw_ean2(upc,resize=1,hideinfo=(False, False, False),barheight=(47, 53)):
 return create_ean2(upc,None,resize,hideinfo,barheight);

def create_ean2_from_list(upc,outfile,resize=1,hideinfo=(False, False, False),barheight=(48, 54)):
 if(sys.version[0]=="2"):
  if(isinstance(upc, str) or isinstance(upc, unicode)):
   return create_ean2(upc,outfile,resize,hideinfo,barheight);
 if(sys.version[0]=="3"):
  if(isinstance(upc, str)):
   return create_ean2(upc,outfile,resize,hideinfo,barheight);
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
   retlist.append(create_ean2(upc[NumLoop],outfile[NumLoop],resize_val,hideinfo_val,barheight_val));
   NumLoop = NumLoop + 1;
 return retlist;

def draw_ean2_from_list(upc,resize=1,hideinfo=(False, False, False),barheight=(48, 54)):
 if(sys.version[0]=="2"):
  if(isinstance(upc, str) or isinstance(upc, unicode)):
   return draw_ean2(upc,resize,hideinfo,barheight);
 if(sys.version[0]=="3"):
  if(isinstance(upc, str)):
   return draw_ean2(upc,resize,hideinfo,barheight);
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
   drawlist.append(draw_ean2(upc[NumLoop],resize_val,hideinfo_val,barheight_val));
   NumLoop = NumLoop + 1;
 return drawlist;
