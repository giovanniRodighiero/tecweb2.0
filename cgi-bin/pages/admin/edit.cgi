#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/mixins.cgi';
print "Content-type: text/html\n\n";

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $id = $cgi->param("id");

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
  if($collection eq 'anagraphic'){
    return anagraphic;
  }
  if($collection eq 'studyTitles'){
    return studyTitles;
  }
}

my $toPrint = renderForm($collection);
print $toPrint;
