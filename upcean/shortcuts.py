'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2011-2014 Cool Dude 2k - http://idb.berlios.de/
    Copyright 2011-2014 Game Maker 2k - http://intdb.sourceforge.net/
    Copyright 2011-2014 Kazuki Przyborowski - https://github.com/KazukiPrzyborowski

    $FileInfo: shortcuts.py - Last Update: 11/02/2014 Ver. 2.7.3 RC 1  - Author: cooldude2k $
'''

from __future__ import absolute_import, division, print_function, unicode_literals;
import sys, re, upcean.validate, upcean.convert, upcean.support;

'''
// Shortcut Codes by Kazuki Przyborowski
// validate
'''
def validate_checksum(bctype, upc, return_check=False):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.validate, "validate_"+bctype+"_checksum") and callable(getattr(upcean.validate, "validate_"+bctype+"_checksum"))):
  return getattr(upcean.validate, "validate_"+bctype+"_checksum")(upc,return_check);
 if(not hasattr(upcean.validate, "validate_"+bctype+"_checksum") or not callable(getattr(upcean.validate, "validate_"+bctype+"_checksum"))):
  return False;
 return False;
def get_checksum(bctype, upc):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.validate, "get_"+bctype+"_checksum") and callable(getattr(upcean.validate, "get_"+bctype+"_checksum"))):
  return getattr(upcean.validate, "get_"+bctype+"_checksum")(upc);
 if(not hasattr(upcean.validate, "get_"+bctype+"_checksum") or not callable(getattr(upcean.validate, "get_"+bctype+"_checksum"))):
  return False;
 return False;
def fix_checksum(bctype, upc):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.validate, "fix_"+bctype+"_checksum") and callable(getattr(upcean.validate, "fix_"+bctype+"_checksum"))):
  return getattr(upcean.validate, "fix_"+bctype+"_checksum")(upc);
 if(not hasattr(upcean.validate, "fix_"+bctype+"_checksum") or not callable(getattr(upcean.validate, "fix_"+bctype+"_checksum"))):
  return False;
 return False;

'''
// Shortcut Codes by Kazuki Przyborowski
// convert
'''
def make_barcode(bctype, numbersystem, manufacturer, product):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.convert, "make_"+bctype+"_barcode") and callable(getattr(upcean.convert, "make_"+bctype+"_barcode"))):
  return getattr(upcean.convert, "make_"+bctype+"_barcode")(numbersystem, manufacturer, product);
 if(not hasattr(upcean.convert, "make_"+bctype+"_barcode") or not callable(getattr(upcean.convert, "make_"+bctype+"_barcode"))):
  return False;
 return False;
def convert_barcode(intype, outtype, upc):
 if(intype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(outtype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.convert, "convert_barcode_from_"+intype+"_to_"+outtype) and callable(getattr(upcean.convert, "convert_barcode_from_"+intype+"_to_"+outtype))):
  return getattr(upcean.convert, "convert_barcode_from_"+intype+"_to_"+outtype)(upc);
 if(not hasattr(upcean.convert, "convert_barcode_from_"+intype+"_to_"+outtype) or not callable(getattr(upcean.convert, "convert_barcode_from_"+intype+"_to_"+outtype))):
  return False;
 return False;
def print_barcode(bctype, outtype,upc):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.convert, "print_"+bctype+"_barcode") and callable(getattr(upcean.convert, "print_"+bctype+"_barcode"))):
  return getattr(upcean.convert, "print_"+bctype+"_barcode")(upc);
 if(not hasattr(upcean.convert, "print_"+bctype+"_barcode") or not callable(getattr(upcean.convert, "print_"+bctype+"_barcode"))):
  return False;
 return False;
def print_convert_barcode(intype, outtype,upc):
 if(bctype not in upcean.support.supported_barcodes("tuple")):
  return False;
 if(hasattr(upcean.convert, "print_convert_barcode_from_"+intype+"_to_"+outtype) and callable(getattr(upcean.convert, "print_convert_barcode_from_"+intype+"_to_"+outtype))):
  return getattr(upcean.convert, "print_convert_barcode_from_"+intype+"_to_"+outtype)(upc);
 if(not hasattr(upcean.convert, "print_convert_barcode_from_"+intype+"_to_"+outtype) or not callable(getattr(upcean.convert, "print_convert_barcode_from_"+intype+"_to_"+outtype))):
  return False;
 return False;