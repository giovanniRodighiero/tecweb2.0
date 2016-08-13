#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/actions/create.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $layout = getLayout();
sub setTitle{
  if($collection eq 'anagraphic'){
    my $title = qq{
      <h1 class="page-title"> Adding a new Anagraphical Information</h1>
    };
    return $title;
  }
  if($collection eq 'studyTitles'){
    my $title = qq{
      <h1 class="page-title"> Adding a new Study Title</h1>
    };
    return $title;
  }
  if($collection eq 'working'){
    my $title = qq{
      <h1 class="page-title"> Adding a new Working Experience</h1>
    };
    return $title;
  }
  if($collection eq 'contacts'){
    my $title = qq{
      <h1 class="page-title"> Adding a new Contact</h1>
    };
    return $title;
  }
  if($collection eq 'skills'){
    my $title = qq{
      <h1 class="page-title"> Adding a new Skill</h1>
    };
    return $title;
  }
}
my $title = setTitle();
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
  require "cgi-bin/pages/forms/".$collection.".cgi";
  my $html = getForm(0);
  print $layout.$title.$html;
}
renderPage;
