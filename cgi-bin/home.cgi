#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
print "Content-type: text/html\n\n";
require 'cgi-bin/functions.cgi';

stampa('db','anagrafica');
