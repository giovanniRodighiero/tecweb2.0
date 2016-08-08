#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
require 'cgi-bin/functions.cgi';
print "Content-type: text/html\n\n";

$cgi = new CGI;
my $collection = $cgi->param("collection");

sub anagraphic{
  my $anagraphic = qq{
        <form id="" action="../../actions/create.cgi" method="post">
          <fieldset>
            <label for="fieldName">Field Name</label>
            <input type="text" id="fieldName" name="fieldName"/>
            <label for="content">Content</label>
            <input type="text" id="content" name="content"/>
            <input type ="hidden" name="collection" value="$collection" />
            <button type="submit">Create</button>
          </fieldset>
        </form>};
  return $anagraphic;
}
sub studyTitles{
  my $studyTitles = qq{
        <form id="" action="../../actions/create.cgi" method="post">
          <fieldset>
            <label for="fieldName">Year</label>
            <input type="text" id="year" name="year"/>
            <label for="title">Title</label>
            <input type="text" id="title" name="title"/>
            <label for="title">SchoolTitle</label>
            <input type="text" id="school" name="school"/>
            <input type ="hidden" name="collection" value="$collection" />
            <button type="submit">Create</button>
          </fieldset>
        </form>};
  return $studyTitles;
}

sub renderForm{
  my($collection) = @_;
  my $html;
  if($collection eq 'anagraphic'){
    $html = anagraphic;
  }
  if($collection eq 'studyTitles'){
    $html = studyTitles;
  }
  print $html;
}

renderForm($collection);
