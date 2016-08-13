#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getForm{
  my ($edit) = @_;
  my $contactName = $cgi->param("contactName");
  my $value = $cgi->param("value");
  my $isLink = $cgi->param("isLink");
  my $collection = $cgi->param("collection");

  my $working = qq{
          <fieldset>
          <div class="group-input">
            <label for="contactName">Contact's Name</label>
            <input type="text" id="contactName" name="contactName" value="$contactName" />
          </div>
          <div class="group-input">
            <label for="value">Contact's Value</label>
            <input type="text" id="value" name="value" value="$value" />
            </div>
          <div class="group-input">
            <label for="isLink">Is the value a link ?</label>};
warn $isLink;
  if($isLink eq 'true'){
    my $rest = q{<input type="checkbox" id="isLink" name="isLink" value="true" checked="checked" />
    </div>
    <input type ="hidden" name="collection" value="$collection" />
    <input type ="hidden" name="submit" value="submit" />};
    $working = $working.$rest;
  }else{
    my $rest = q{<input type="checkbox" id="isLink" name="isLink" value="true" />
    </div>
    <input type ="hidden" name="collection" value="$collection" />
    <input type ="hidden" name="submit" value="submit" />};
    $working = $working.$rest;
  }
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
        <p>Admin Panel<a href="home.cgi">Home</a> /<a href="contacts.cgi">Contacts and Socials</a> / <span class="active"> Update Contact</span></p>
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="contacts.cgi">Contacts and Socials</a> / <span class="active"> New Contact</span></p>
    </div>
    <form class="form" action="new.cgi" method="post">
  };
}
  return $path.$working.$ending;
}
return 1;
