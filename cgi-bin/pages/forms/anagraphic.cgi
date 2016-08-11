#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getCreationForm{
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my $collection = $cgi->param("collection");
  my $anagraphic = qq{
        <form id="" action="new.cgi" method="post">
          <fieldset>
            <label for="fieldName">Field Name</label>
            <input type="text" id="fieldName" name="fieldName" value="$fieldName" />
            <label for="content">Content</label>
            <input type="text" id="content" name="content" value="$content" />
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="submit" value="submit" />
            <button type="submit">Create</button>
          </fieldset>
        </form>};
  return $anagraphic;
}
sub getEditionForm{
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my $collection = $cgi->param("collection");
  my $id = $cgi->param("id");
  my $anagraphic = qq{
        <form id="" action="edit.cgi" method="post">
          <fieldset>
            <label for="fieldName">Field Name</label>
            <input type="text" id="fieldName" name="fieldName" value="$fieldName" />
            <label for="content">Content</label>
            <input type="text" id="content" name="content" value="$content" />
            <input type ="hidden" name="collection" value="$collection" />
            <input type ="hidden" name="id" value="$id" />
            <input type ="hidden" name="submit" value="submit" />
            <button type="submit">Update</button>
          </fieldset>
        </form>};
  return $anagraphic;
}
return 1;
