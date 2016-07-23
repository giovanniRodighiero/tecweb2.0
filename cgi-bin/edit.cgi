#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/functions.cgi';

$cgi = new CGI;

my $item_name = $cgi->param("item_name");
my $text = $cgi->param("text");
insert('anagraphic',$item_name, $text);
print $cgi->header(-location =>'home.cgi',-refresh => '0; home.cgi' );# così non riaggiunge il commento con refresh pagina

print $testo;
