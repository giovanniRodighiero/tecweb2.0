#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/functions.cgi';

print "Content-type: text/html\n\n";
$cgi = new CGI;

my $testo = $cgi->param("test");#contiene il testo della form

stampa('db','anagrafica_write');
print $testo;
