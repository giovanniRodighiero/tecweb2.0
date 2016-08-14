#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
use CGI::Session;

require 'cgi-bin/mixins.cgi';
require 'cgi-bin/globals.cgi';
require 'cgi-bin/pages/forms/login.cgi';
$cgi = new CGI;
my $user = $cgi->param("username");
my $pass = $cgi->param("password");
my $layout = getLayout('Login','Login page','Login');

sub renderPage{
  if(getSession() ne undef){
    print $session->header(-refresh => '0; ../admin/home.cgi' );
  }
  if(($user eq undef) and ($pass eq undef)){
    print "Content-type: text/html\n\n";
    printLoginForm(0);
  }else{
    if(checkLogin()){
      $session = new CGI::Session();
      $session->param('id', $user);
      print $session->header(-refresh => '0; ../admin/home.cgi' );
    }else{
      print "Content-type: text/html\n\n";
      printLoginForm(1);
    }
  }
}
sub printLoginForm{
  my ($error) = @_;
  my $form = getLoginForm();
  my $html = $layout.$form;
  if($error){
    $html = $html."<span class=\"error\">Wrong username or password</span></body></html>";
  }
  $html = $html."<a class=\"back-home\" href=\"home.cgi\">Back to home</a></body></html>";
  print $html;
}

sub checkLogin(){
  my $valid=0;
  open(IN, "public_html/info") or die("errore col file");
  while(<IN>) {
    if( /^$user\:$pass$/ ) {
      $valid = 1;
      last;
    }
  }
  close(IN);
  return $valid;
}
renderPage();
