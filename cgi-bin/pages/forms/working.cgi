#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getForm{
  my ($edit) = @_;
  my $begin =$cgi->param("begin");
  my $end =$cgi->param("end");
  my $role =$cgi->param("role");
  my $company =$cgi->param("company");
  my $collection = $cgi->param("collection");
  my $working = qq{
    <form class="form" action="new.cgi" method="post">
      <fieldset>
      <div class="group-input">
        <label for="begin">Year of begin</label>
        <input type="text" id="begin" name="begin" value="$begin"/>
      </div>
      <div class="group-input">
        <label for="end">Year of end</label>
        <input type="text" id="end" name="end" value="$end"/>
      </div>
      <div class="group-input">
        <label for="role">Perfomed role</label>
        <input type="text" id="role" name="role" value="$role"/>
      </div>
      <div class="group-input">
        <label for="company">Company name</label>
        <input type="text" id="company" name="company" value="$company"/>
      </div>
        <input type ="hidden" name="collection" value="$collection" />
        <input type ="hidden" name="submit" value="submit" />
      };
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="working.cgi">Working Experiences</a> / <span class="active"> Update Working Experience</span></p>
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="working.cgi">Working Experiences</a> / <span class="active"> New Working Experience</span></p>
    </div>
  };
}
  return $path.$working.$ending;
}
return 1;
