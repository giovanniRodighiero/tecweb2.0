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
  my @ids = ('year','title','school');
  my $collection = $cgi->param("collection");
  my $studyTitles = qq{
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
  if($edit == 1){
    my $id = $cgi->param("id");
    $ending = qq{
    <input type ="hidden" name="id" value="$id" />
    <button type="submit">Update</button>
    </fieldset>
  </form>
  <div>
  <button type="reset" class="reset" onclick="return clearForm('@ids');"> Clear Form</button>
  </div>
};
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="studyTitles.cgi">Study Titles and Education</a> / <span class="active"> Update Study Titles</span></p>
    </div>
    <form class="form" action="edit.cgi" method="post">
  };
}
if($edit == 0){
  $ending = qq{
    <button type="submit">Create</button>
    </fieldset>
  </form>
  <div>
  <button type="reset" class="reset" onclick="return clearForm('@ids');"> Clear Form</button>
  </div>
  };
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="studyTitles.cgi.cgi">Study Titles and Education</a> / <span class="active"> New Study Title</span></p>
    </div>
    <form class="form" action="new.cgi" method="post">
  };
}
if($edit == 2){
  my $id = $cgi->param("id");
  $studyTitles = qq{
    <fieldset>
    <input type ="hidden" name="collection" value="$collection" />
  };
  $ending = qq{
  <input type ="hidden" name="id" value="$id" />
  <button type="submit">Delete</button>
  </fieldset>
</form>};
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="studyTitles.cgi">Study Titles and Education</a> / <span class="active"> Delete Study Titles and Education</span></p>
    </div>
    <div class="box-delete">
      <div>
        <span class="key">Title's name</span>
        <p class="value">$title</p>
      </div>
      <div>
        <span class="key">Year of attainment</span>
        <p class="value">$year</p>
      </div>
      <div>
        <span class="key">School</span>
        <p class="value">$school</p>
      </div>
    </div>
    <form class="form" action="../../destroy.cgi" method="post">
  };
}
  return $path.$studyTitles.$ending;
}
return 1;
