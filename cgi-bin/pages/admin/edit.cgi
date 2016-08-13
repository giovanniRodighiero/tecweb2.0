#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/mixins.cgi';
require 'cgi-bin/actions/update.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $id = $cgi->param("id");
my $layout = getLayout();

sub setTitle{
  if($collection eq 'anagraphic'){
    my $title = qq{
      <h1 class="page-title"> Updating an Anagraphical Information</h1>
    };
    return $title;
  }
  if($collection eq 'studyTitles'){
    my $title = qq{
      <h1 class="page-title"> Updating a Study Title</h1>
    };
    return $title;
  }
  if($collection eq 'working'){
    my $title = qq{
      <h1 class="page-title"> Updating a Working Experience</h1>
    };
    return $title;
  }
  if($collection eq 'contacts'){
    my $title = qq{
      <h1 class="page-title"> Updating a Contact</h1>
    };
    return $title;
  }
  if($collection eq 'skills'){
    my $title = qq{
      <h1 class="page-title"> Updating a Skill</h1>
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
    print $cgi->header(-location =>'edit.cgi',-refresh => '0; home.cgi' );
  }else{
    if($cgi->param("submit") eq ""){# came here from the home page => the form is rendered
      print "Content-type: text/html\n\n";
      renderForm($collection);
      print $cancel."</body></html>"
    }else{# came here after the submit of the creation form => validation
      @errors = update();
      if(scalar @errors > 0){
        print "Content-type: text/html\n\n";
        renderForm($collection);
        print printErrors(@errors);
        print $cancel."</body></html>"
      }else{
        print $cgi->header(-location =>'edit.cgi',-refresh => '0; '.$collection.'.cgi' );
      }
    }
  }
}

sub renderForm{
  my($collection) = @_;
  require "cgi-bin/pages/forms/".$collection.".cgi";
  my $html = getForm(1);
  print $layout.$title.$html;
}
renderPage;
