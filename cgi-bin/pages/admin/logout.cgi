#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
use CGI::Session;

require '../../mixins.cgi';
require '../../globals.cgi';
require '../../pages/forms/login.cgi';

my $logout = $cgi->param("logout");

sub renderPage{
  if($logout eq "logout"){
    destroySession();

  }else{
    print "Content-type: text/html\n\n";
    printLogoutForm();
  }
}
sub destroySession() {
  $session = CGI::Session->load() or die $!;
  $SID = $session->id();
  $session->close();
  $session->delete();
  $session->flush();
  print $cgi->header(-location =>'../public/home.cgi');
}
my $layout = getLayout('Logout', 'Logout page', 'Logout');
sub printLogoutForm{
  my $form = getLogoutForm();
  my $html = $layout.$form;

  $html = $html."<div><a class=\"back-home\" href=\"home.cgi\"> Cancel </a></div></body></html>";
  print $html;
}

  renderPage();
