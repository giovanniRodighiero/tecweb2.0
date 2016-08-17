#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
require "../../mixins.cgi";
require "../../globals.cgi";

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
  @errors = validate($title, "Title's Name", true, @errors);
  @errors = validate($school, "School", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<year>".$year."</year>\n\t\t<title>".$title."</title>\n\t\t<school>".$school."</school> \n\t</item>\n";
    $query="//".$collection;
    appendFragment($query, $new_node);
  }
  return @errors;
}
sub buildWorkingNode{
  my ($collection, $begin, $end, $role, $company) = @_;
  my @errors;
  @errors = validate($begin, "Year of beginning", true, @errors);
  @errors = validate($end, "Year of ending", true, @errors);
  @errors = validate($role, "Perfomed Role", true, @errors);
  @errors = validate($company, "Company Name", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<begin>".$begin."</begin>\n\t\t<end>".$end."</end>\n\t\t<role>".$role."</role>\n\t\t<company>".$company."</company> \n\t</item>\n";
    $query="//".$collection;
    appendFragment($query, $new_node);
  }
  return @errors;
}
sub buildContactNode{
  my ($collection, $contactName, $value, $isLink) = @_;
  warn $isLink;
  my @errors;
  @errors = validate($contactName, "Contact's Name", true, @errors);
  @errors = validate($value, "Contact's value", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<contactName>".$contactName."</contactName>\n\t\t<value isLink=\"".$isLink."\">".$value."</value>\n\t</item>\n";
    $query="//".$collection;
    appendFragment($query, $new_node);
    warn "dentro";
  }
  return @errors;
}
sub buildSkillsNode{
  my ($collection, $skillName, $level) = @_;
  my @errors;
  @errors = validate($skillName, "Skill's Name", true, @errors);
  @errors = validate($level, "Level's content", true, @errors);
  if(scalar @errors < 1){
    my $next_id = generateNextId('//'.$collection.'/item[last()]');
    my $new_node = "\t<item id=\"".$next_id."\">\n\t\t<skillsName>".$skillName."</skillsName>\n\t\t<level>".$level."</level>\n\t</item>\n";
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
  if($collection eq 'working'){
    my $begin =$cgi->param("begin");
    my $end =$cgi->param("end");
    my $role =$cgi->param("role");
    my $company =$cgi->param("company");
    @errors = buildWorkingNode($collection, $begin, $end, $role, $company);
  }
  if($collection eq 'contacts'){
    my $contactName =$cgi->param("contactName");
    my $value =$cgi->param("value");
    my $isLink =$cgi->param("isLink");
    @errors = buildContactNode($collection, $contactName, $value, $isLink);
  }
  if($collection eq 'skills'){
    my $skillsName =$cgi->param("skillsName");
    my $level =$cgi->param("level");
    @errors = buildSkillsNode($collection, $skillsName, $level);
  }
  if(scalar @errors < 1){
    open(OUT, ">$fileDati");
    print OUT $doc->toString;
    close(OUT);
  }
  return @errors;
}
