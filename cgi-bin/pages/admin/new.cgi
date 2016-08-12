#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/actions/create.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");

sub renderPage{
  if($collection eq ""){# came here by a simple link or manually typing the url => redirect
    print $cgi->header(-location =>'new.cgi',-refresh => '0; home.cgi' );
  }else{
    if($cgi->param("submit") eq ""){# came here from the home page => the form is rendered
      print "Content-type: text/html\n\n";
      renderForm($collection);
    }else{# came here after the submit of the creation form => validation
      my @errors = buildNode();
      warn @errors;
      if(@errors != 0){
        warn scalar @errors;
        print "Content-type: text/html\n\n";
        print printErrors(@errors);
        renderForm($collection);
      }else{
        print $cgi->header(-location =>'new.cgi',-refresh => '0; '.$collection.'.cgi' );
      }
    }
  }
}

sub renderForm{
  my($collection) = @_;
  my $html;
  if($collection eq 'anagraphic'){
    require "cgi-bin/pages/forms/anagraphic.cgi";
    $html = getCreationForm();
  }
  if($collection eq 'studyTitles'){
    require "cgi-bin/pages/forms/studyTitles.cgi";
    $html = getCreationForm();
  }
  print $html;
}
renderPage;
