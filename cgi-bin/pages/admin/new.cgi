#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/actions/create.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $layout;
sub setTitle{
  if($collection eq 'anagraphic'){
    $layout = getLayout('New Anagraphic Field', 'Page that adds a new anagraphic field', 'New Anagraphic Field');
    my $title = qq{
      <h1 class="page-title"> Adding a new Anagraphical Information</h1>
    };
    return $title;
  }
  if($collection eq 'studyTitles'){
    $layout = getLayout('New Study Title Field', 'Page that adds a new study title field', 'New Study Title Field, Education');
    my $title = qq{
      <h1 class="page-title"> Adding a new Study Title</h1>
    };
    return $title;
  }
  if($collection eq 'working'){
    $layout = getLayout('New Working Experience Field', 'Page that adds a new working experience field', 'New Working Experience Field');
    my $title = qq{
      <h1 class="page-title"> Adding a new Working Experience</h1>
    };
    return $title;
  }
  if($collection eq 'contacts'){
    $layout = getLayout('New Contact Field', 'Page that adds a new contact field', 'New Contact Field');
    my $title = qq{
      <h1 class="page-title"> Adding a new Contact</h1>
    };
    return $title;
  }
  if($collection eq 'skills'){
    $layout = getLayout('New Skill Field', 'Page that adds a new skill field', 'New Skill Field');
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
      print $cancel."<script type=\"text/javascript\" src=\"../../../public_html/javascript/main.js\">//</script></body></html>"
    }else{# came here after the submit of the creation form => validation
      my @errors = buildNode();
      if(@errors > 0){
        print "Content-type: text/html\n\n";
        renderForm($collection);
        print printErrors(@errors);
        print $cancel."<script type=\"text/javascript\" src=\"../../../public_html/javascript/main.js\"</script></body></html>"
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
