<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Contacts and Socials Admin - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Contacts and Socials"/>
      <meta name="description" content="Contacts and Social Networks profiles of Giovanni Rodighiero."/>
      <meta name="keywords" content="Contacts, Socials, Social Networks, Email, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="working">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p>Admin Panel<a href="home.cgi">Home</a><span class="active">/ Contacts and Socials</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="home.cgi" accesskey="o"><span class="accesskey">O</span>verview</a></li>
            <li><a href="anagraphic.cgi" accesskey="a">Edit <span class="accesskey">A</span>nagraphical Informations</a></li>
            <li><a href="studyTitles.cgi" accesskey="s">Edit <span class="accesskey">S</span>tudy Titles and Education</a></li>
            <li><a href="working.cgi" accesskey="w">Edit <span class="accesskey">W</span>orking Experience</a></li>
            <li><a href="skills.cgi" accesskey="k">Edit S<span class="accesskey">k</span>ills and Languages</a></li>
            <li><span class="active">Edit <span class="accesskey">C</span>ontacts and Socials</span></li>
          </ul>
        </div>
        <div id="content">
          <div class="box-full">
            <xsl:apply-templates select="contacts"/>
          </div>
        </div><a class="back-top" href="#content">Back to top</a>
        <div id="footer"><a class="admin" href="login.cgi">Admin area</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
        <script type="text/javascript" src="../../../javascript/main.js">//</script>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="contacts">
    <div id="modal-div">
      <h2>Proceed with the deletion ?</h2>
      <form class="inline" action="../../actions/destroy.cgi" method="post">
        <fieldset class="inline" id="modal">
          <button type="submit" id="modal-submit">Confirm</button>
        </fieldset>
      </form>
      <button class="inline">
        <xsl:attribute name="onclick">return cancelModal("<xsl:value-of select="@id" />", "contacts");
</xsl:attribute>Cancel
      </button>
    </div>
    <div>
      <h2 class="page-title">Contacts and Socials</h2>
      <form class="form" action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="contacts"/>
          <button type="submit">New Contacts</button>
        </fieldset>
      </form>
    </div>
    <div>
      <ul>
        <xsl:for-each select="item">
          <li>
            <div class="item">
              <div><span class="key">
                  <xsl:value-of select="contactName"></xsl:value-of></span>
                <p class="value">
                  <xsl:choose>
                    <xsl:when test="value/@isLink = 'true'"><a class="external-link">
                        <xsl:attribute name="href">
                          <xsl:value-of select="value"/>
                        </xsl:attribute>
                        <xsl:value-of select="value"/></a></xsl:when>
                    <xsl:otherwise>
                      <xsl:value-of select="value"/>
                    </xsl:otherwise>
                  </xsl:choose>
                </p>
              </div>
              <form class="form inline-form" action="edit.cgi" method="post">
                <fieldset>
                  <input type="hidden" name="collection" value="contacts"/>
                  <input type="hidden" name="id" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="@id" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="contactName" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="contactName" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="value" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="value" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="isLink" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="value/@isLink" />
                    </xsl:attribute>
                  </input>
                  <button type="submit"> Edit </button>
                </fieldset>
              </form>
              <form class="form inline-form" action="delete.cgi" method="post"><xsl:attribute name="onclick">return renderModal("<xsl:value-of select="@id" />", "contacts");
</xsl:attribute>
                <fieldset>
                  <input type="hidden" name="collection" value="contacts"/>
                  <input type="hidden" name="id" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="@id" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="contactName" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="contactName" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="value" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="value" />
                    </xsl:attribute>
                  </input>
                  <input type="hidden" name="isLink" >
                    <xsl:attribute name="value">
                      <xsl:value-of select="value/@isLink" />
                    </xsl:attribute>
                  </input>
                  <button type="submit"> Delete </button>
                </fieldset>
              </form>
            </div>
          </li>
        </xsl:for-each>
      </ul>
    </div>
  </xsl:template>
</xsl:stylesheet>