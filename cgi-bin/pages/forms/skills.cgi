#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getForm{
  my ($edit) = @_;
  my $level = $cgi->param("level");
  my $skillsName = $cgi->param("skillsName");
  my $collection = $cgi->param("collection");
  my $skills = qq{
          <fieldset>
          <div class="group-input">
            <label for="skillName">Skill's Name</label>
            <input type="text" id="skillName" name="skillsName" value="$skillsName" />
          </div>
          <div class="group-input">
            <label for="level">Level of Knowledge</label>
            <input type="text" id="level" name="level" value="$level" />
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
        <p>Admin Panel<a href="home.cgi">Home</a> /<a href="skills.cgi">Skills and Languages</a> / <span class="active"> Update Skills and Languages</span></p>
      </div>
      <form class="form" action="edit.cgi" method="post">
    };
}else{
  $ending = qq{
    <button type="submit">Create</button>
    </fieldset>
  </form>
  };
  $path = qq{
    <div id="path">
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="skills.cgi">Skills and Languages</a> / <span class="active"> New Skills and Languages</span></p>
    </div>
    <form class="form" action="new.cgi" method="post">
  };
}
  return $path.$skills.$ending;
}
return 1;
