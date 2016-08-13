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
  @errors = validate($item_name, "Field's Name", true, @errors);
  @errors = validate($text, "Field's content", true, @errors);
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
  my @errors;
  @errors = validate($year, "Year of attainment", true, @errors);
  @errors = validate($title, "Title's Name", true, @errors);
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
sub working{
  my ($collection, $id, $begin, $end, $role, $company) = @_;
  my @errors;
  @errors = validate($begin, "Year of beginning", true, @errors);
  @errors = validate($end, "Year of ending", true, @errors);
  @errors = validate($role, "Perfomed Role", true, @errors);
  @errors = validate($company, "Company Name", true, @errors);
  if(scalar @errors < 1){
    #update Begin fiels
    my $begin_query="//".$collection."/item[\@id = \"".$id."\"]/begin/text()";
    updateNode($begin_query, $begin);

    # update end field
    my $end_query="//".$collection."/item[\@id = \"".$id."\"]/end/text()";
    updateNode($end_query, $end);

    # update role field
    my $role_query="//".$collection."/item[\@id = \"".$id."\"]/role/text()";
    updateNode($role_query, $role);

    # update company field
    my $company_query="//".$collection."/item[\@id = \"".$id."\"]/company/text()";
    updateNode($company_query, $company);
  }
  return @errors;
}
sub contacts{
  warn "qua";
  my ($collection, $id, $contactName, $value, $isLink) = @_;
  my @errors;
  @errors = validate($contactName, "Contact's Name", true, @errors);
  @errors = validate($value, "Contact's value", true, @errors);
  if(scalar @errors < 1){
    #update contactName fiels
    my $contactName_query="//".$collection."/item[\@id = \"".$id."\"]/contactName/text()";
    updateNode($contactName_query, $contactName);

    # update value field
    my $value_query="//".$collection."/item[\@id = \"".$id."\"]/value";
    my $node = $root->findnodes($value_query)->get_node(1);
    my $parent = $node->parentNode;
    $parent->removeChild($node);
    $new_value = "<value isLink=\"".$isLink."\">".$value."</value>";
    $fragment = $parser->parse_balanced_chunk($new_value);
    $parent->appendChild($fragment);
  }
  return @errors;
}

sub update{
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");
  warn "dentro update";
  warn $collection;
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
  if($collection eq 'working'){
    my $begin =$cgi->param("begin");
    my $end =$cgi->param("end");
    my $role =$cgi->param("role");
    my $company =$cgi->param("company");
    @errors = working($collection, $id, $begin, $end, $role, $company);
  }
  if($collection eq 'contacts'){
    warn "dentro contacts";
    my $contactName =$cgi->param("contactName");
    my $value =$cgi->param("value");
    my $isLink =$cgi->param("isLink");
    @errors = contacts($collection, $id, $contactName, $value, $isLink);
  }
  if(scalar @errors < 1){
    open(OUT, ">$fileDati");
    print OUT $doc->toString;
    close(OUT);
  }
  return @errors;
}
