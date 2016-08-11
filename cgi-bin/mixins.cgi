
sub myPrint{
  my ($xslName, $read_write) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $trasformata='public_html/xsl/'.$xslName.'/'.$read_write.'.xsl';
	my $xslt = XML::LibXSLT->new();
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $query="//".$xslName;
  my $node = $doc->findnodes($query)->get_node(1);
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina =$stylesheet->output_as_bytes($risultato);
  return $nuovaPagina;
}
sub validate{
  my ($value, $fieldName, $notEmpty, @errors) = @_;
  if($value eq undef && $notEmpty){
    my $message = "The value of the field \'".$fieldName."\' cannot be empty.";
    push(@errors, $message);
  }else{
  if($value =~m/\//){
    my $message = "The field \'".$fieldName."\' contains forbidden characters (/).";
		push(@errors, $message);
	}
	if($value =~m/>/){
    my $message = "The field \'".$fieldName."\' contains forbidden characters (>).";
    push(@errors, $message);
		}
	if($value =~m/</){
    my $message = "The field \'".$fieldName."\' contains forbidden characters (<).";
    push(@errors, $message);
		}
  }
  return @errors;
}
sub printErrors{
  my (@errors) = @_;
  my $html = qq{
    <div>
      <h2> Unable to perform the request</h2>
      <p> Make sure to respect the following rules:</p>
      <ul>
  };
  for( $a = 0; $a < @errors; $a = $a + 1 ){
      $html =  $html."<li>@errors[$a]</li>";
    }
  $html = $html."</ul></div>";
  return $html;
}
1;
