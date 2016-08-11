#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/mixins.cgi';

print "Content-type: text/html\n\n";

my $anagraphic = myPrint('anagraphic', 'write');

#print qq{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n};
#print qq{<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">};
print $anagraphic;
#print "</html>";
