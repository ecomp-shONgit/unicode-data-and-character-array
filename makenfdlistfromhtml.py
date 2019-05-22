
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, string, time, codecs, os

# 2012, eAqua Dissimination Project, Prof. Charlotte Schubert Alte Geschichte Leipzig
# Source of NFD (!): http://www.unicode.org/charts/normalization/, see folder "htmlfromunicodeorg"
# Purpose: program builds a cvs style list ";;" seperated to save the unicode normalization data and character codes
# CSV style: "unicodenameofcombined letter";;"unicodenumbercombined";;"unicodeletter";;"NFDunicodeletternumbers"
# Purpose 2: program builds a JS array of NFC to NFC unicode normalform of the characters 


def makelist( path, naming):
    gf = open( path )
    gft = gf.read( )
    gf.close()
    
    gfttable = gft.split("<table>")[ 1 ].split("<tr>")
    out = ""
    outjavascriptarray = ""
    for i in xrange( len( gfttable ) ):
        if i > 1:
            unicodenameofcombined = 'NULL'
            unicodenumbercombined = 'NULL'
            unicodeletter = 'NULL'
            NFDunicodeletters = 'NULL'
            
            apart = gfttable[ i ].split( ">" )
            for j in xrange( len( apart ) ):
                if j == 0:
                    unicodenameofcombined = apart[ j ].split( "<" )[ 1 ].split( '"' )[ 3 ]
                if j == 1:
                    unicodeletter = apart[ j ].split( "<" )[ 0 ]
                if j == 3:
                    unicodenumbercombined = apart[ j ].split( "<" )[ 0 ]
                if j == 13:
                    NFDunicodeletters = apart[ j ].split( "<" )[ 0 ]
            out = out + ( "%s;;%s;;%s;;%s\n" % (unicodenameofcombined, unicodenumbercombined, unicodeletter, NFDunicodeletters) )
            outjavascriptarray = outjavascriptarray + 'utf8_nfd["\u%s"] =  "\u%s";\n' % (unicodenumbercombined, "\u".join( NFDunicodeletters.split( " " ) ) )
    #print 
    outg = open( naming + ".csv", "w" )
    outg.write( out )
    outg.close( )
    outgjs = open( naming + ".js", "w" )
    outgjs.write( outjavascriptarray )
    outgjs.close( )

if __name__ == '__main__':
    print ( "On." )
    
    ##
    #greek
    makelist( "htmlfromunicodeorg/greek.html", "greek")
    #latin
    makelist( "htmlfromunicodeorg/latin.html", "latin")
    #arabic
    makelist( "htmlfromunicodeorg/arabic.html", "arabic")
    #hebrew
    makelist( "htmlfromunicodeorg/hebrew.html", "hebrew")
    ##
    
    print ( "Off." )

    
    
    
