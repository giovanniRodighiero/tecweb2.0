#!/usr/bin/perl
#!/usr/bin/perl -w
use XML::LibXSLT;
use XML::LibXML;
use CGI;
$cgi = new CGI;
sub getLoginForm{
  my $username = $cgi->param("username");
  my $login = qq{
        <div id="loginForm">
        <form id="" action="login.cgi" method="post">
          <fieldset>
            <label for="username">Username</label>
            <input type="text" id="username" name="username" value="$username" />
            <label for="password">Password</label>
            <input type="password" id="password" name="password"  />
            <button type="submit">Log in</button>
          </fieldset>
        </form>
      </div>};
  return $login;
}
sub getLogoutForm{
  my $logout = qq{
        <div id="logoutForm">
        <h2> Confirm to logout </h2>
        <form id="" action="logout.cgi" method="post">
          <fieldset>
            <input type="hidden" name="logout" value="logout" />
            <button type="submit">Log out</button>
          </fieldset>
        </form>
        <a href="home.cgi"> Cancel </a>
      </div>};
  return $logout;
}

return 1;
