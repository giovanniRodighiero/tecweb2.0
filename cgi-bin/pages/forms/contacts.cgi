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

  my $contact = qq{
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
  if($isLink eq 'true'){
    my $rest = qq{<input type="checkbox" id="isLink" name="isLink" value="true" checked="checked" />
    </div>
    <input type ="hidden" name="collection" value="$collection" />
    <input type ="hidden" name="submit" value="submit" />};
    $working = $working.$rest;
  }else{
    my $rest = qq{<input type="checkbox" id="isLink" name="isLink" value="true" />
    </div>
    <input type ="hidden" name="collection" value="$collection" />
    <input type ="hidden" name="submit" value="submit" />};
    $working = $working.$rest;
  }
  my $ending;
  my $path;
  if($edit == 1){
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
}
if($edit == 0){
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
if($edit == 2){
  my $id = $cgi->param("id");
  $contact = qq{
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
      <p>Admin Panel<a href="home.cgi">Home</a> /<a href="contacts.cgi">Contacts and Socials</a> / <span class="active"> Delete Contacts and Socials</span></p>
    </div>
    <div class="box-delete">
      <div>
        <span class="key">Contact's name</span>
        <p class="value">$contactName</p>
      </div>
      <div>
        <span class="key">Contact's value</span>
        <p class="value">$value</p>
      </div>
    </div>
    <form class="form" action="../../destroy.cgi" method="post">
  };
}
  return $path.$contact.$ending;
}
return 1;
