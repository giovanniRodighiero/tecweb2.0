#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
print "Content-type: text/html\n\n";
print "<H1>Hello World</H1>\n";
stampa();
sub stampa{
  my $fileDati='public_html/db.xml';
  my $trasformata='public_html/db.xsl';
  my $parser = XML::LibXML->new();
	my $xslt = XML::LibXSLT->new();

	my $doc = $parser->parse_file($fileDati);
  my $query="//catalog";
  my $node = $doc->findnodes($query)->get_node();
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina =$stylesheet->output_as_bytes($risultato);
  print $nuovaPagina;
}
