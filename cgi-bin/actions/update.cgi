#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;

sub anagraphic{
  my($collection ,$id, $fieldName, $content) = @_;
  print $id;
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");
  # update fieldName field
  $fieldName_query="//".$collection."/item[\@id = \"".$id."\"]/fieldName/text()";
  my $fieldName_node = $root->findnodes($fieldName_query)->get_node(1);
  $fieldName_node->setData($fieldName);
  #update content field
  $content_query="//".$collection."/item[\@id = \"".$id."\"]/content/text()";
  my $content_node = $root->findnodes($content_query)->get_node(1);
  $content_node->setData($content);
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
}

sub update{
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    anagraphic($collection, $id, $fieldName, $content);
  }
}
update();
print $cgi->header(-location =>'update.cgi',-refresh => '0; ../pages/home.cgi' );
