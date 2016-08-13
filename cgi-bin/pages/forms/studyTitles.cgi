#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getForm{
  my ($edit) = @_;
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
        <input type ="hidden" name="submit" value="submit" />};
  my $ending;
  my $path;
  if($edit){
    my $id = $cgi->param("id");
    $ending = qq{
    <input type ="hidden" name="id" value="$id" />
    <button type="submit">Update</button>
    </fieldset>
  </form>};
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="studyTitles.cgi">Study Titles and Education</a> / <span class="active"> Update Study Titles</span></p>
    </div>
  };
}else{
  $ending = qq{
    <button type="submit">Create</button>
    </fieldset>
  </form>
  };
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="studyTitles.cgi.cgi">Study Titles and Education</a> / <span class="active"> New Study Title</span></p>
    </div>
  };
}
  return $path.$studyTitles.$ending;
}
return 1;
