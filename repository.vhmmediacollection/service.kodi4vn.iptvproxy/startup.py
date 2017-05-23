#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask , request , redirect
import re , json , urllib
import requests , YDStreamExtractor
from operator import itemgetter
requests . packages . urllib3 . disable_warnings ( )
YDStreamExtractor . disableDASHVideo ( True )
if 64 - 64: i11iIiiIii
OO0o = Flask ( __name__ )
if 81 - 81: Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o
@ OO0o . route ( '/play' )
def ii11i ( ) :
 return oOooOoO0Oo0O ( )
 if 10 - 10: IIiI1I11i11
@ OO0o . route ( '/play.m3u8' )
def oOooOoO0Oo0O ( ) :
 ooOO00oOo = ""
 try :
  ooOO00oOo = request . args . get ( "url" )
 except : return ""
 if "livestream.com" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   if "events" not in ooOO00oOo :
    Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
    IiIi11iIIi1Ii = re . search ( "accounts/\d+/events/\d+" , Oooo000o . text )
    ooOO00oOo = "https://livestream.com/api/%s" % IiIi11iIIi1Ii . group ( )
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   Oo0O = Oooo000o . json ( )
   ooOO00oOo = Oo0O [ "stream_info" ] [ "m3u8_url" ]
  except : pass
 elif "ustream.tv" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   IiI = re . search ( "tv/embed/(\d+)" , Oooo000o . text ) . group ( 1 )
   ooOO00oOo = "http://iphone-streaming.ustream.tv/uhls/%s/streams/live/iphone/playlist.m3u8" % IiI
  except : pass
 elif "youtube.com" in ooOO00oOo :
  OOOo0 = {
 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0' ,
 'Accept-Encoding' : 'gzip, deflate' ,
 }
  try :
   Oooo000o = requests . get ( ooOO00oOo , headers = OOOo0 )
   IiIi11iIIi1Ii = re . search ( '"hlsvp":".+?"' , Oooo000o . text )
   Oo0O = json . loads ( '{%s}' % IiIi11iIIi1Ii . group ( ) )
   ooOO00oOo = Oo0O [ "hlsvp" ]
  except :
   try :
    ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( )
   except : pass
 elif "vtvgo-" in ooOO00oOo :
  ooOo = ooOO00oOo . split ( "-" ) [ - 1 ]
  ooOO00oOo = "http://vtvgo.vn/get-program-channel-detail?epg_id=%s&id=%s&type=1" % ( ooOo , ooOo )
  OOOo0 = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 }
  if 91 - 91: Ii1I . OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
  O0oO = requests . get ( "aHR0cDovL3Z0dmdvLnZuL3hlbS10cnVjLXR1eWVuLmh0bWw=" . decode ( "base64" ) , headers = OOOo0 )
  o0oO0 = re . compile ( "'(\w{32})'\)\;" ) . findall ( O0oO . text . encode ( "utf8" ) ) [ 0 ]
  try :
   oo00 = re . compile ( 'epg_id=(\d+)' ) . findall ( ooOO00oOo ) [ 0 ]
   o00 = re . compile ( 'type=(\d+)' ) . findall ( ooOO00oOo ) [ 0 ]
   OOOo0 = {
 "X-Requested-With" : "XMLHttpRequest" ,
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
 "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8" ,
 "Accept-Encoding" : "gzip, deflate" ,
 "Referer" : "http://vtvgo.vn/" ,
 "Cookie" : "csrf_security=1"
 }
   Oo0oO0ooo = {
 "epg_id" : oo00 ,
 "type" : o00 ,
 "secret_token" : o0oO0 ,
 "csrf_security" : "1"
 }
   o0oOoO00o = requests . post ( ooOO00oOo , headers = OOOo0 , data = Oo0oO0ooo ) . json ( )
   ooOO00oOo = o0oOoO00o [ "data" ]
  except : pass
 elif "facebook.com" in ooOO00oOo :
  i1 = re . search ( "videos/(\d+)" , ooOO00oOo ) . group ( 1 )
  ooOO00oOo = "https://www.facebook.com/video/playback/playlist.m3u8?v=%s" % i1
 elif "twitch.tv" in ooOO00oOo :
  try :
   oOOoo00O0O = "|User-Agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0"
   ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( ) . split ( "|" ) [ 0 ] + oOOoo00O0O
  except : pass
 elif "://" not in ooOO00oOo :
  if ooOO00oOo . startswith ( "uno-" ) :
   i1111 = ooOO00oOo . strip ( ) . replace ( "uno-" , "" )
   i11 = "NTg4N2RkZmZjMzEyYmYxMDk0ZGU0YmQ1" . decode ( "base64" )
   I11 = {
 "Content-Type" : "application/x-www-form-urlencoded" ,
 "User-Agent" : "Dalvik/2.1.0" ,
 "Accept-Encoding" : "gzip"
 }
   Oo0o0000o0o0 = {
 "serial_id" : i11 ,
 "query" : i1111
 }
   oOo0oooo00o = requests . post (
 "http://stbapi.v247tv.com/api/stb_channel2" ,
 headers = I11 ,
 data = Oo0o0000o0o0
 ) . json ( ) [ "data" ]
   oO0o0o0ooO0oO = requests . get ( "aHR0cDovL2VjaGlwc3RvcmUuY29tOjgwMDAvdW5vLw==" . decode ( "base64" ) + urllib . quote_plus ( oOo0oooo00o ) )
   Oo0O = re . compile ( "(\{.+?\})" ) . findall ( oO0o0o0ooO0oO . text . strip ( ) ) [ 0 ]
   ooOO00oOo = json . loads ( Oo0O ) [ "url" ]
   if "smil:" in ooOO00oOo :
    oo0o0O00 = re . search ( 'https*://.+?/' , ooOO00oOo ) . group ( )
   else :
    oo0o0O00 = ooOO00oOo . split ( "playlist" ) [ 0 ]
   oO = requests . get ( ooOO00oOo ) . text . strip ( )
   ooOO00oOo = oo0o0O00 + i1iiIIiiI111 ( oO )
  elif ooOO00oOo . startswith ( "beeb-" ) :
   i1111 = ooOO00oOo . strip ( ) . replace ( "beeb-" , "" )
   oooOOOOO = {
 "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" ,
 "X-Requested-With" : "XMLHttpRequest" ,
 "Accept-Encoding" : "gzip, deflate, sdch"
 }
   if 22 - 22: oOO * OooooO0oOO + IiIi11i
   O0oO = requests . get (
 "http://tv.beeb.vn/site/player?channel=" + i1111 ,
 headers = oooOOOOO )
   iIii1I111I11I = re . search ( 'stream = "(.+?)"' , O0oO . text ) . group ( 1 )
   ooOO00oOo = iIii1I111I11I if "http://" in iIii1I111I11I else "http://tv.beeb.vn" + iIii1I111I11I
   ooOO00oOo = requests . head (
 ooOO00oOo ,
 headers = oooOOOOO ) . headers [ "location" ]
  else :
   OO00OooO0OO = requests . get ( "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRDaGFubmVsc0FwcEJveC5waHA=" . decode ( "base64" ) ) . json ( )
   for iiiIi in OO00OooO0OO [ "channels" ] :
    if iiiIi [ "channel_url" ] == ooOO00oOo :
     IiIIIiI1I1 = "aHR0cDovL3d3dy52aWV0dHYyNC5jb20vbWFpbi9nZXRTdHJlYW1pbmdTZXJ2ZXIucGhw" . decode ( "base64" )
     oOo0oooo00o = { 'strname' : '%s-' % iiiIi [ "channel_id" ] }
     ooOO00oOo = requests . post ( IiIIIiI1I1 , data = oOo0oooo00o ) . text . strip ( )
     oO = requests . get ( ooOO00oOo ) . text . strip ( )
     oo0o0O00 = re . search ( 'https*://.+?/.+?/.+?/' , ooOO00oOo ) . group ( )
     ooOO00oOo = oo0o0O00 + i1iiIIiiI111 ( oO )
 else :
  try :
   ooOO00oOo = YDStreamExtractor . getVideoInfo ( ooOO00oOo ) . streamURL ( )
  except : pass
 print "beeb_stream: " + ooOO00oOo
 return redirect ( ooOO00oOo )
 if 86 - 86: i11I1IIiiIi + oOo + iiIiIiIi - o0oooO0OO0O / IiIi11i
def i1iiIIiiI111 ( text ) :
 IiIi11iIIi1Ii = re . compile ( 'BANDWIDTH=(\d+),.+?\n(.+?)$' , re . M ) . findall ( text )
 oo = [ ]
 for Ii11iI1i , Ooo in IiIi11iIIi1Ii :
  oo += [ [ int ( Ii11iI1i ) , Ooo ] ]
 oo = sorted ( oo , key = itemgetter ( 0 ) )
 return oo [ - 1 ] [ - 1 ]
 if 68 - 68: OooooO0oOO + oOO . OO0O0O - oOo % OO0O0O - o0oooO0OO0O
if __name__ == '__main__' :
 OO0o . run ( host = '0.0.0.0' , threaded = True ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
