sub stampa{
  my ($collection, $xslName) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $trasformata='public_html/xsl/'.$xslName.'.xsl';
  my $parser = XML::LibXML->new();
	my $xslt = XML::LibXSLT->new();

	my $doc = $parser->parse_file($fileDati);
  my $query="//".$collection;
  my $node = $doc->findnodes($query)->get_node();
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina =$stylesheet->output_as_bytes($risultato);
  print $nuovaPagina;
}
sub buildAnagraphicNode{
  my ($node, $item_name, $text) = @_;
  my $new_node = "\t<item>\n\t\t<fieldName>".$item_name."</fieldName>\n\t\t<content>".$text."</content>\n\t</item>\n";
  return $new_node;
}

sub insert{
  my ($collection, $item_name, $text) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");
  $query="//".$collection;
  my $node = $root->findnodes($query)->get_node(1);
  my $new_node;
  warn $collection;
  if($collection eq 'anagraphic'){
    $new_node = buildAnagraphicNode(@_);
  }
  my $fragment = $parser->parse_balanced_chunk($new_node);
  	$node->appendChild($fragment) || die("");
    open(OUT, ">$fileDati");
    print OUT $doc->toString;
    close(OUT);
    #$testo=undef;
}
1;
