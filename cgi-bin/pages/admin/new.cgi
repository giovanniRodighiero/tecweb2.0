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
      @errors = buildNode();
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

sub anagraphic{
  my $anagraphic = qq{
        <form id="" action="new.cgi" method="post">
          <fieldset>
            <label for="fieldName">Field Name</label>
            <input type="text" id="fieldName" name="fieldName"/>
            <label for="content">Content</label>
            <input type="text" id="content" name="content"/>
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="submit" value="submit" />
            <button type="submit">Create</button>
          </fieldset>
        </form>};
  return $anagraphic;
}
sub studyTitles{
  my $studyTitles = qq{
        <form id="" action="new.cgi" method="post">
          <fieldset>
            <label for="fieldName">Year</label>
            <input type="text" id="year" name="year"/>
            <label for="title">Title</label>
            <input type="text" id="title" name="title"/>
            <label for="title">SchoolTitle</label>
            <input type="text" id="school" name="school"/>
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="submit" value="submit" />
            <button type="submit">Create</button>
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
    $html = studyTitles;
  }
  print $html;
}
renderPage;
