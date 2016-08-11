#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
use CGI::Session;

require 'cgi-bin/mixins.cgi';
require 'cgi-bin/pages/forms/login.cgi';

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
  print $cgi->header(-location =>'logout.cgi',-refresh => '0; ../public/home.cgi' );
}
sub printLogoutForm{
  my $form = getLogoutForm();
  my $html = $layout.$form;
  $html = $html."</body></html>";
  print $html;
}
my $layout = qq{
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
    <title>Logout - Giovanni Rodighiero Resume</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="title" content="Giovanni Rodighiero Resume - Logout"/>
    <meta name="description" content="Logout the admin area of the website that presents Giovanni Rodighiero's resume."/>
    <meta name="keywords" content="Logout, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
    <meta name="author" content="Giovanni Rodighiero"/>
    <meta name="language" content="english en"/>
    <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
    <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
  };
  renderPage();
