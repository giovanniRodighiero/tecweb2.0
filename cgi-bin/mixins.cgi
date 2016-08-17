use CGI::Session;

sub myPrint{
  my ($xslName, $read_write) = @_;
  my $fileDati='public_html/xml/db.xml';
  my $trasformata='public_html/xsl/'.$xslName.'/'.$read_write.'.xsl';
	my $xslt = XML::LibXSLT->new();
  my $parser = XML::LibXML->new();
  my $doc = $parser->parse_file($fileDati);
  my $query="/";
  my $node = $doc->findnodes($query)->get_node(1);
	my $xslt_doc = $parser->parse_file($trasformata);
	my $stylesheet = $xslt->parse_stylesheet($xslt_doc);
	my $risultato = $stylesheet->transform($node);
	my $nuovaPagina = qq{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
  };
  $nuovaPagina = $nuovaPagina.$stylesheet->output_as_bytes($risultato);

  $nuovaPagina = $nuovaPagina."</html>";
  return $nuovaPagina;
}
sub validate{
  my ($value, $fieldName, $notEmpty, @errors) = @_;
  if($value eq undef && $notEmpty){
    my $message = "The value of the field \'".$fieldName."\' cannot be empty.";
    push(@errors, $message);
  }else{
  if($value =~m/\// and ($fieldName ne 'Contact\'s value')){
    warn $fieldName;
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
    <div class="error">
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

sub getSession{
   $session = CGI::Session->load() or die $!;
  if ($session->is_expired || $session->is_empty ) {
      return undef;
  } else {
    my $utente = $session->param("id");
    return $utente;
  }
}
1;
