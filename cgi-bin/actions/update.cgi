#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;

sub anagraphic{
  my($collection ,$id, $fieldName, $content) = @_;
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
sub studyTitles{
  my($collection ,$id, $year, $title, $school) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $root = $doc->getDocumentElement || die("Non accedo alla radice");
  #update year field
  $year_query="//".$collection."/item[\@id = \"".$id."\"]/year/text()";
  my $year_node = $root->findnodes($year_query)->get_node(1);
  $year_node->setData($year);
  # update title field
  $title_query="//".$collection."/item[\@id = \"".$id."\"]/title/text()";
  my $title_node = $root->findnodes($title_query)->get_node(1);
  $title_node->setData($title);
  # update school field
  $school_query="//".$collection."/item[\@id = \"".$id."\"]/school/text()";
  my $school_node = $root->findnodes($school_query)->get_node(1);
  $school_node->setData($school);

  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
}

my $collection = $cgi->param("collection");
my $id = $cgi->param("id");

sub update{
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    anagraphic($collection, $id, $fieldName, $content);
  }
  if($collection eq 'studyTitles'){
    my $year =$cgi->param("year");
    my $title =$cgi->param("title");
    my $school =$cgi->param("school");
    studyTitles($collection, $id, $year, $title, $school);
  }
}
update();
print $cgi->header(-location =>'update.cgi',-refresh => '0; ../pages/admin/home.cgi' );
