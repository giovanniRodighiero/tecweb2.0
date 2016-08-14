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
sub getLayout{
  my ($title, $descr, $keywords) = @_;
  my $layout = qq{
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n
      <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
      <head>
      <title>$title - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - $title"/>
      <meta name="description" content="$descr of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="$keywords, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
      </head>
      <body>
    };
  return $layout;
}
