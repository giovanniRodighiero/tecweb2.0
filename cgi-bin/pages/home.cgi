#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/functions.cgi';

print "Content-type: text/html\n\n";

myPrint('db','anagraphic','read');

myPrint('db','anagraphic', 'write');
