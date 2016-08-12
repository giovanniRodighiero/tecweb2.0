#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
require "cgi-bin/mixins.cgi";
require "cgi-bin/globals.cgi";

my $fileDati = getFileData();
my $parser = getParser();
my $doc = getDoc();
my $root = getRoot();


sub appendFragment{
  my ($query, $new_node) = @_;
  my $node = $root->findnodes($query)->get_node(1);
  my $fragment = $parser->parse_balanced_chunk($new_node);
  $node->appendChild($fragment) || die("");
}
sub buildAnagraphicNode{
  my ($collection, $item_name, $text) = @_;
  my @errors;
  @errors = validate($item_name, "Field's Name", true, @errors);
  @errors = validate($text, "Field's content", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<fieldName>".$item_name."</fieldName>\n\t\t<content>".$text."</content>\n\t</item>\n";
    $query="//".$collection;
    appendFragment($query, $new_node);
  }
  return @errors;
}
sub buildStudyTitlesNode{
  my ($collection, $year, $title, $school) = @_;
  my @errors;
  @errors = validate($year, "Year of attainment", true, @errors);
  @errors = validate($title, "Title", true, @errors);
  @errors = validate($school, "School", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<year>".$year."</year>\n\t\t<title>".$title."</title>\n\t\t<school>".$school."</school> \n\t</item>\n";
    $query="//".$collection;
    appendFragment($query, $new_node);
  }
  return @errors;
}

sub generateNextId{
  my($query) = @_;
  my $node = $doc->findnodes($query)->get_node(1);
  if($node eq undef){
    return 1;
  }else{
    my $oldId = $node->getAttribute("id");
    return $oldId+1;
  }
}

sub buildNode{
  my $collection = $cgi->param("collection");
  my @errors;
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    @errors = buildAnagraphicNode($collection, $fieldName, $content);
  }
  if($collection eq 'studyTitles'){
    my $year =$cgi->param("year");
    my $title =$cgi->param("title");
    my $school =$cgi->param("school");
    @errors = buildStudyTitlesNode($collection, $year, $title, $school);
  }
  warn @errors;
  if(scalar @errors < 1){
    open(OUT, ">$fileDati");
    print OUT $doc->toString;
    close(OUT);
  }
  return @errors;
}
