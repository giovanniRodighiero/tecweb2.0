

sub getDoc{
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  return $doc;
}
sub myPrint{
  my ($xslName, $read_write) = @_;
  my $trasformata='public_html/xsl/'.$xslName.'/'.$read_write.'.xsl';
	my $xslt = XML::LibXSLT->new();
  my $parser = XML::LibXML->new();
	my $doc = getDoc();
  my $query="//".$xslName;
  my $node = $doc->findnodes($query)->get_node(1);
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina =$stylesheet->output_as_bytes($risultato);
  return $nuovaPagina;
}
1;
