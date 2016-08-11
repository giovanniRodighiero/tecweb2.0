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

sub updateNode{
  my ($query, $data) = @_;
  my $node = $root->findnodes($query)->get_node(1);
  $node->setData($data);
}

sub anagraphic{
  my($collection ,$id, $fieldName, $content) = @_;
  my @errors;
  warn $id;
  @errors = validate($fieldName, "Field's Name", true, @errors);
  @errors = validate($content, "Field's content", true, @errors);
  if(scalar @errors < 1){
  # update fieldName field
  $fieldName_query="//".$collection."/item[\@id = \"".$id."\"]/fieldName/text()";
  warn "FLAG  ";

  updateNode($fieldName_query, $fieldName);
  #update content field
  $content_query="//".$collection."/item[\@id = \"".$id."\"]/content/text()";
  updateNode($content_query, $content);
  }
  return @errors;
}
sub studyTitles{
  my($collection ,$id, $year, $title, $school) = @_;
  
  @errors = validate($year, "Year", true, @errors);
  @errors = validate($title, "Title", true, @errors);
  @errors = validate($school, "School", true, @errors);
  if(scalar @errors < 1){
    #update year field
    $year_query="//".$collection."/item[\@id = \"".$id."\"]/year/text()";
    updateNode($year_query, $year);

    # update title field
    $title_query="//".$collection."/item[\@id = \"".$id."\"]/title/text()";
    updateNode($title_query, $title);

    # update school field
    $school_query="//".$collection."/item[\@id = \"".$id."\"]/school/text()";
    updateNode($school_query, $school);
  }
  return @errors;
}

sub update{
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");
  my @errors;
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    @errors = anagraphic($collection, $id, $fieldName, $content);
  }
  if($collection eq 'studyTitles'){
    my $year =$cgi->param("year");
    my $title =$cgi->param("title");
    my $school =$cgi->param("school");
    @errors = studyTitles($collection, $id, $year, $title, $school);
  }
  if(scalar @errors < 1){
    open(OUT, ">$fileDati");
    print OUT $doc->toString;
    close(OUT);
  }
  return @errors;
}
