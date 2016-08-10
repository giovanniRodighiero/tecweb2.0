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

sub renderPage{
  if($collection eq ""){# came here by a simple link or manually typing the url => redirect
    print $cgi->header(-location =>'new.cgi',-refresh => '0; home.cgi' );
  }else{
    if($cgi->param("submit") eq ""){# came here from the home page => the form is rendered
      print "Content-type: text/html\n\n";
      renderForm($collection);
    }else{# came here after the submit of the creation form => validation
      @errors = update();
      if(scalar @errors > 0){
        print "Content-type: text/html\n\n";
        print printErrors(@errors);
        renderForm($collection);
      }else{
        print $cgi->header(-location =>'new.cgi',-refresh => '0; home.cgi' );
      }
    }
  }
}

sub anagraphic {
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my $anagraphic = qq{
        <form id="" action="../../actions/update.cgi" method="post">
          <fieldset>
            <label for="fieldName">Field Name</label>
            <input type="text" id="fieldName" name="fieldName" value="$fieldName" />
            <label for="content">Content</label>
            <input type="text" id="content" name="content" value="$content" />
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="id" value="$id" />
            <button type="submit">Save</button>
          </fieldset>
        </form>};
  return $anagraphic;
}
sub studyTitles {
  my $year = $cgi->param("year");
  my $title = $cgi->param("title");
  my $school = $cgi->param("school");
  my $studyTitles = qq{
        <form id="" action="../../actions/update.cgi" method="post">
          <fieldset>
            <label for="year">Year</label>
            <input type="text" id="year" name="year" value="$year" />
            <label for="title">Title</label>
            <input type="text" id="title" name="title" value="$title" />
            <label for="school">School</label>
            <input type="text" id="school" name="school" value="$school" />
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="id" value="$id" />
            <button type="submit">Save</button>
          </fieldset>
        </form>};
  return $studyTitles;
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
