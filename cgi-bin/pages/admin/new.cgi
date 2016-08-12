#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/actions/create.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $layout = getLayout();
my $title = qq{
  <h1 class="page-title"> Adding a new Anagraphical Information</h1>
};
my $cancel = qq{
  <a href="$collection.cgi" class="back-home"> Cancel </a>
};
sub renderPage{
  if($collection eq ""){# came here by a simple link or manually typing the url => redirect
    print $cgi->header(-location =>'new.cgi',-refresh => '0; home.cgi' );
  }else{
    if($cgi->param("submit") eq ""){# came here from the home page => the form is rendered
      print "Content-type: text/html\n\n";
      renderForm($collection);
      print $cancel."</body></html>"
    }else{# came here after the submit of the creation form => validation
      my @errors = buildNode();
      warn @errors;
      if(@errors != 0){
        warn scalar @errors;
        print "Content-type: text/html\n\n";
        renderForm($collection);
        print printErrors(@errors);
        print $cancel."</body></html>"
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
  print $layout.$title.$html;
}
renderPage;
