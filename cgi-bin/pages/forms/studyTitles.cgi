#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getCreationForm{
  my $year =$cgi->param("year");
  my $title =$cgi->param("title");
  my $school =$cgi->param("school");
  my $collection = $cgi->param("collection");
  my $studyTitles = qq{
    <form class="form" action="new.cgi" method="post">
      <fieldset>
      <div class="group-input">
        <label for="fieldName">Year of attainment</label>
        <input type="text" id="year" name="year" value="$year"/>
      </div>
      <div class="group-input">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" value="$title"/>
      </div>
      <div class="group-input">
        <label for="title">School</label>
        <input type="text" id="school" name="school" value="$school"/>
      </div>
        <input type ="hidden" name="collection" value="$collection" />
        <input type ="hidden" name="submit" value="submit" />
        <button type="submit">Create</button>
      </fieldset>
    </form>};
  return $studyTitles;
}
sub getEditionForm{
  my $year =$cgi->param("year");
  my $title =$cgi->param("title");
  my $school =$cgi->param("school");
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");
  my $studyTitles = qq{
    <form class="form" action="edit.cgi" method="post">
      <fieldset>
      <div class="group-input">
        <label for="fieldName">Year</label>
        <input type="text" id="year" name="year" value="$year"/>
      </div>
      <div class="group-input">
        <label for="title">Title</label>
        <input type="text" id="title" name="title" value="$title"/>
      </div>
      <div class="group-input">
        <label for="title">SchoolTitle</label>
        <input type="text" id="school" name="school" value="$school"/>
      </div>
        <input type ="hidden" name="collection" value="$collection" />
        <input type ="hidden" name="id" value="$id" />
        <input type ="hidden" name="submit" value="submit" />
        <button type="submit">Update</button>
      </fieldset>
    </form>};
  return $studyTitles;
}
return 1;
