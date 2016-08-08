#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;

sub anagraphic{
  my($id) = @_;
  my $query="//anagraphic/item[\@id = \"".$id."\"]";
  return $query;
}
sub studyTitles{
  my($id) = @_;
  my $query="//studyTitles/item[\@id = \"".$id."\"]";
  return $query;
}


sub destroyNode{
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");

  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");
  my $query;
  if($collection eq 'anagraphic'){
    $query = anagraphic($id);
  }
  if($collection eq 'studyTitles'){
    $query = studyTitles($id);
  }
  my $node = $root->findnodes($query)->get_node(1);
  my $parent = $node->parentNode;
  $parent->removeChild($node);
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
}

destroyNode();
print $cgi->header(-location =>'destroy.cgi',-refresh => '0; ../pages/admin/home.cgi' );
