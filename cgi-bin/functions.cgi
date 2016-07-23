sub stampa{
  my ($node, $xslName) = @_;

  my $fileDati='public_html/xml/db.xml';
  my $trasformata='public_html/xsl/'.$xslName.'.xsl';
  my $parser = XML::LibXML->new();
	my $xslt = XML::LibXSLT->new();

	my $doc = $parser->parse_file($fileDati);
  my $query="//".$node;
  my $node = $doc->findnodes($query)->get_node();
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina =$stylesheet->output_as_bytes($risultato);
  print $nuovaPagina;
}

1;
