#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/mixins.cgi';

$cgi = new CGI;


my $user = getSession();
if($user eq undef){
  print $cgi->header(-location =>'home.cgi',-refresh => '0; ../public/home.cgi' );
}else{
  print "Content-type: text/html\n\n";
  my $skills = myPrint('skills', 'write');
  print $skills;
}
