#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
use CGI::Session;

require 'cgi-bin/mixins.cgi';
require 'cgi-bin/pages/forms/login.cgi';
$cgi = new CGI;
my $user = $cgi->param("username");
my $pass = $cgi->param("password");
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
my $layout = qq{
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
    <title>Login - Giovanni Rodighiero Resume</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="title" content="Giovanni Rodighiero Resume - Login"/>
    <meta name="description" content="Login to the admin area of the website that presents Giovanni Rodighiero's resume."/>
    <meta name="keywords" content="Login, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
    <meta name="author" content="Giovanni Rodighiero"/>
    <meta name="language" content="english en"/>
    <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
    <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
  };

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
