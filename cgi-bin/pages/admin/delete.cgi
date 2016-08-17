#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require '../../mixins.cgi';
require '../../globals.cgi';

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $layout;
sub setTitle{
  if($collection eq 'anagraphic'){
    $layout = getLayout('Delete Anagraphic Field', 'Page that deletes an anagraphic field', 'Delete Anagraphic Field');
    my $title = qq{
      <h1 class="page-title"> Deleting an Anagraphical Information</h1>
    };
    return $title;
  }
  if($collection eq 'studyTitles'){
    $layout = getLayout('Delete a Study Title Field', 'Page that deletes a study title field', 'Delete Study Title Field, Education');
    my $title = qq{
      <h1 class="page-title"> Deleting a Study Title</h1>
    };
    return $title;
  }
  if($collection eq 'working'){
    $layout = getLayout('Delete Working Experience Field', 'Page that deletes a working experience field', 'Delete Working Experience Field');
    my $title = qq{
      <h1 class="page-title"> Deleting a Working Experience</h1>
    };
    return $title;
  }
  if($collection eq 'contacts'){
    $layout = getLayout('Delete Contact Field', 'Page that deletes a contact field', 'Delete Contact Field');
    my $title = qq{
      <h1 class="page-title"> Deleting a Contact</h1>
    };
    return $title;
  }
  if($collection eq 'skills'){
    $layout = getLayout('Delete Skill Field', 'Page that deletes a skill field', 'Delete Skill Field');
    my $title = qq{
      <h1 class="page-title"> Deleting a Skill</h1>
    };
    return $title;
  }
}
my $title = setTitle();
my $cancel = qq{
  <div>
  <a href="$collection.cgi" class="back-home"> Cancel </a>
  </div>
};
sub renderPage{
  if($collection eq ""){# came here by a simple link or manually typing the url => redirect
    print $cgi->header(-location =>'home.cgi');
  }else{
    if($cgi->param("submit") eq ""){# came here from the home page => the form is rendered
      print "Content-type: text/html\n\n";
      renderForm($collection);
      print $cancel."</body></html>"
    }else{
        print $cgi->header(-location =>$collection.'.cgi');
      }
    }
  }


sub renderForm{
  my($collection) = @_;
  require "../forms/".$collection.".cgi";
  my $html = getForm(2);
  print $layout.$title.$html;
}
renderPage;
