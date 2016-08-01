#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;

sub buildAnagraphicNode{
  my ($collection, $item_name, $text) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");

  my $next_id = generateNextId($doc, '//'.$collection.'/item[last()]');
  my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<fieldName>".$item_name."</fieldName>\n\t\t<content>".$text."</content>\n\t</item>\n";

  $query="//".$collection;
  my $node = $root->findnodes($query)->get_node(1);
  my $fragment = $parser->parse_balanced_chunk($new_node);
  $node->appendChild($fragment) || die("");
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
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
  my $collection = $cgi->param("collection");
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    buildAnagraphicNode($collection, $fieldName, $content);
  }
}
insert();
print $cgi->header(-location =>'create.cgi',-refresh => '0; ../pages/home.cgi' );
