#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require '../../mixins.cgi';

$cgi = new CGI;


my $user = getSession();
if($user eq undef){
  print $cgi->header(-location =>'../public/home.cgi');
}else{
  print "Content-type: text/html\n\n";
  my $contacts = myPrint('contacts', 'write');
  print $contacts;
}
