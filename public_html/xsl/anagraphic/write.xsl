<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <title>titolo</title>
    </head>
    <body>
      <div id="homepage">
        <div id="header">
          <h1>Giovanni Rodighiero Resume</h1>
        </div>
        <div id="nav">
          <ul>
            <li class="active">Edit Anagraphic</li>
            <li><a href="#">Edit Study Titles</a></li>
            <li><a href="#">Edit Working Experience</a></li>
          </ul>
        </div>
        <div id="content">
          <xsl:apply-templates select="anagraphic"/>
        </div>
        <div id="footer"><a href="#">Log out</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="anagraphic">
    <div>
      <form action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="anagraphic"/>
          <button type="submit">New Anagraphic Info</button>
        </fieldset>
      </form>
    </div>
    <ul>
      <xsl:for-each select="item">
        <li>
          <div><span class="key">Field Name</span>
            <p class="value">
              <xsl:value-of select="fieldName"/>
            </p>
          </div>
          <div><span class="key">Field Content</span>
            <p class="value">
              <xsl:value-of select="content"/>
            </p>
          </div>
          <form action="edit.cgi" method="post">
            <fieldset>
              <input type="hidden" name="collection" value="anagraphic"/>
              <input type="hidden" name="id" >
                <xsl:attribute name="value">
                  <xsl:value-of select="@id" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="fieldName" >
                <xsl:attribute name="value">
                  <xsl:value-of select="fieldName" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="content" >
                <xsl:attribute name="value">
                  <xsl:value-of select="content" />
                </xsl:attribute>
              </input>
              <button type="submit"> Edit </button>
            </fieldset>
          </form>
          <form action="delete.cgi" method="post">
            <fieldset>
              <input type="hidden" name="collection" value="anagraphic"/>
              <input type="hidden" name="id" >
                <xsl:attribute name="value">
                  <xsl:value-of select="@id" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="fieldName" >
                <xsl:attribute name="value">
                  <xsl:value-of select="fieldName" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="content" >
                <xsl:attribute name="value">
                  <xsl:value-of select="content" />
                </xsl:attribute>
              </input>
              <button type="submit"> Delete </button>
            </fieldset>
          </form>
        </li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>