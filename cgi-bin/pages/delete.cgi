#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;

print "Content-type: text/html\n\n";

$cgi = new CGI;
my $collection = $cgi->param("collection");
my $id = $cgi->param("id");

sub anagraphic{
  my $fieldName = $cgi->param("fieldName");
  my $content = $cgi->param("content");
  my $anagraphic = qq{
        <div>
          <h3> Proceed with the deletion of this field ? </h3>
          <span>$fieldName:</span><span>$content</span>
          <form id="" action="../actions/destroy.cgi" method="post">
            <fieldset>
              <input type ="hidden" name="collection" value="$collection" />
              <input type ="hidden" name="id" value="$id" />
              <button type="submit">Delete</button>
            </fieldset>
          </form>
          <a href="home.cgi"> Cancel </a>
        </div>
        };
  return $anagraphic;
}

sub renderConfirm{
  my($collection) = @_;
  if($collection eq 'anagraphic'){
   return anagraphic;
  }
}

my $confirmPage = renderConfirm($collection);
print $confirmPage;
