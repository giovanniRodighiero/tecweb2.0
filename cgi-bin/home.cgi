#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/functions.cgi';

print "Content-type: text/html\n\n";

stampa('db','anagraphic_read');

stampa('db','anagraphic_write');
