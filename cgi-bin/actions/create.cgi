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

sub buildNode{
  my $collection = $cgi->param("collection");
  if($collection eq 'anagraphic'){
    my $fieldName =$cgi->param("fieldName");
    my $content =$cgi->param("content");
    buildAnagraphicNode($collection, $fieldName, $content);
  }
  if($collection eq 'studyTitles'){
    my $year =$cgi->param("year");
    my $title =$cgi->param("title");
    my $school =$cgi->param("school");
    buildStudyTitlesNode($collection, $year, $title, $school);
  }
  open(OUT, ">$fileDati");
  print OUT $doc->toString;
  close(OUT);
}
sub buildAnagraphicNode{
  my ($collection, $item_name, $text) = @_;

  my $next_id = generateNextId('//'.$collection.'/item[last()]');
  my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<fieldName>".$item_name."</fieldName>\n\t\t<content>".$text."</content>\n\t</item>\n";

  $query="//".$collection;
  my $node = $root->findnodes($query)->get_node(1);
  my $fragment = $parser->parse_balanced_chunk($new_node);
  $node->appendChild($fragment) || die("");
}
sub buildStudyTitlesNode{
  my ($collection, $year, $title, $school) = @_;

  my $next_id = generateNextId('//'.$collection.'/item[last()]');
  my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<year>".$year."</year>\n\t\t<title>".$title."</title>\n\t\t<school>".$school."</school> \n\t</item>\n";

  $query="//".$collection;
  my $node = $root->findnodes($query)->get_node(1);
  my $fragment = $parser->parse_balanced_chunk($new_node);
  $node->appendChild($fragment) || die("");
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

buildNode();
print $cgi->header(-location =>'create.cgi',-refresh => '0; ../pages/admin/home.cgi' );
