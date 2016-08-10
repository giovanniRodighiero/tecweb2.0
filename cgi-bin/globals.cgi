#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;

use strict; use warnings;

my $fileDati='public_html/xml/db.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileDati);
my $root = $doc->getDocumentElement || die("Non accedo alla radice");

sub getFileData{
  return $fileDati;
}
sub getParser {
  return $parser;
}
sub getDoc {
  return $doc;
}
sub getRoot {
  return $root;
}
