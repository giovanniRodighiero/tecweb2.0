#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;


my $fileDati='../../public_html/xml/db.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($fileDati);
my $root = $doc->getDocumentElement || die("Non accedo alla radice");

sub getQuery{
  my($id, $collection) = @_;
  my $query="//".$collection."/item[\@id = \"".$id."\"]";
  return $query;
}

sub destroyNode{
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");

  my $query = getQuery($id, $collection);
  my $node = $root->findnodes($query)->get_node(1);
  my $parent = $node->parentNode;
  $parent->removeChild($node);
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
  print $cgi->header(-location =>'../pages/admin/'.$collection.'.cgi');
}

destroyNode();
