#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getForm{
  my ($edit) = @_;
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my @ids = ('fieldName', 'contentt');

  my $collection = $cgi->param("collection");
  my $anagraphic = qq{
          <fieldset>
          <div class="group-input">
            <label for="fieldName">Field's Name</label>
            <input type="text" id="fieldName" name="fieldName" value="$fieldName" />
          </div>
          <div class="group-input">
            <label for="contentt">Field's Content</label>
            <input type="text" id="contentt" name="content" value="$content" />
            </div>
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="submit" value="submit" />};
  my $ending;
  my $path;
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="anagraphic.cgi">Anagraphical Informations</a> / <span class="active"> New Anagraphical Information</span></p>
    </div>
    <form class="form" action="new.cgi" method="post">
  };
}
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="anagraphic.cgi">Anagraphical Informations</a> / <span class="active"> Update Anagraphical Information</span></p>
    </div>
    <form class="form" action="edit.cgi" method="post">
  };
}
if($edit == 2){
  my $id = $cgi->param("id");
  $anagraphic = qq{
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="anagraphic.cgi">Anagraphical Informations</a> / <span class="active"> Delete Anagraphical Information</span></p>
    </div>
    <div class="box-delete">
      <span class="key">$fieldName</span>
      <p class="value">$content</p>
    </div>
    <form class="form" action="../../actions/destroy.cgi" method="post">
  };
}
  return $path.$anagraphic.$ending;
}
return 1;
