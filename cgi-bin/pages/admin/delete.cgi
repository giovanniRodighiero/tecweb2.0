#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;

print "Content-type: text/html\n\n";

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $id = $cgi->param("id");

sub anagraphic{
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my $anagraphic = qq{
        <div>
          <h3> Proceed with the deletion of this field ? </h3>
          <span>$fieldName:</span><span>$content</span>
          <form id="" action="../../actions/destroy.cgi" method="post">
            <fieldset>
              <input type ="hidden" name="collection" value="$collection" />
              <input type ="hidden" name="id" value="$id" />
              <button type="submit">Delete</button>
            </fieldset>
          </form>
          <a href="home.cgi"> Cancel </a>
        </div>
        };
  return $anagraphic;
}
sub studyTitles{
  my $year = $cgi->param("year");
  my $title = $cgi->param("title");
  my $school = $cgi->param("school");
  my $studyTitles = qq{
        <div>
          <h3> Proceed with the deletion of this study title ? </h3>
          <span>$year</span><span>$title</span><span>$school</span>
          <form id="" action="../../actions/destroy.cgi" method="post">
            <fieldset>
              <input type ="hidden" name="collection" value="$collection" />
              <input type ="hidden" name="id" value="$id" />
              <button type="submit">Delete</button>
            </fieldset>
          </form>
          <a href="home.cgi"> Cancel </a>
        </div>
        };
  return $studyTitles;
}

sub renderConfirm{
  my($collection) = @_;
  if($collection eq 'anagraphic'){
   return anagraphic;
  }
  if($collection eq 'studyTitles'){
   return studyTitles;
  }
}

my $confirmPage = renderConfirm($collection);
print $confirmPage;
