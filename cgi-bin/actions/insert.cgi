require 'cgi-bin/functions.cgi';

sub buildAnagraphicNode{
  my ($collection, $item_name, $text) = @_;
  my $doc = getDoc();
  my $next_id = generateNextId($doc, '//'.$collection.'/item[last()]');

  my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<fieldName>".$item_name."</fieldName>\n\t\t<content>".$text."</content>\n\t</item>\n";
  return $new_node;
}

sub generateNextId{
  my($doc, $query) = @_;
  my $node = $doc->findnodes($query)->get_node(1);
  if($node eq undef){
    return 1;
  }else{
    my $oldId = $node->getAttribute("id");
    return $oldId+1;
  }
}
sub insert{
  my ($collection) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");
  $query="//".$collection;
  my $node = $root->findnodes($query)->get_node(1);
  my $new_node;
  if($collection eq 'anagraphic'){
    $new_node = buildAnagraphicNode(@_);
  }
  my $parser = XML::LibXML->new();
  my $fragment = $parser->parse_balanced_chunk($new_node);
	$node->appendChild($fragment) || die("");
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
}
