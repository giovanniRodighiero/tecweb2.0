#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/mixins.cgi';

print "Content-type: text/html\n\n";

my $skills = myPrint('skills', 'read');
print $skills;
