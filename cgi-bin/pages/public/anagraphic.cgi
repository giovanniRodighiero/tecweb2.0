#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require '../../mixins.cgi';

print "Content-type: text/html\n\n";

my $anagraphic = myPrint('anagraphic', 'read');
print $anagraphic;
