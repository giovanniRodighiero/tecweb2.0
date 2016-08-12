#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;

require "cgi-bin/globals.cgi";

my $fileDati = getFileData();
my $parser = getParser();
my $doc = getDoc();
my $root = getRoot();

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
  print $cgi->header(-location =>'destroy.cgi',-refresh => '0; ../pages/admin/'.$collection.'.cgi' );
}

destroyNode();
