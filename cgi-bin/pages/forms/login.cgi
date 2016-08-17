#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getLoginForm{
  my $username = $cgi->param("username");
  my $login = qq{
        <div class="form">
        <h1> Access to the admin area </h1>
        <form  action="login.cgi" method="post">
          <fieldset>
            <div class="group-input">
              <label for="username">Username</label>
              <input type="text" id="username" name="username" value="$username" />
            </div>
            <div class="group-input">
              <label for="password">Password</label>
              <input type="password" id="password" name="password"  />
            </div>
            <div class="group-input">
              <button type="submit">Log in</button>
            </div>
          </fieldset>
        </form>
      </div>};
  return $login;
}
sub getLogoutForm{
  my $logout = qq{
        <div class="form">
        <h1> Confirm to logout </h1>
        <form  action="logout.cgi" method="post">
          <fieldset>
            <input type="hidden" name="logout" value="logout" />
            <div class="group-input">
              <button type="submit">Confirm</button>
            </div>
          </fieldset>
        </form>
      </div>};
  return $logout;
}

return 1;
