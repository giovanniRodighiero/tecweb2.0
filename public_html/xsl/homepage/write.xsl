<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head></head>
    <body>
      <div id="homepage">
        <div id="header">
          <h1>Giovanni Rodighiero Resume</h1>
        </div>
        <div id="nav">
          <ul>
            <li><a href="#">Edit Anagraphic</a></li>
            <li><a href="#">Edit Study Titles</a></li>
            <li><a href="#">Edit Working Experience</a></li>
          </ul>
        </div>
        <div id="content">
          <div><img src="../../../public_html/images/photo.png"/></div>
          <div>
            <xsl:apply-templates select="anagraphic"/>
          </div>
          <div>
            <xsl:apply-templates select="studyTitles"/>
          </div>
        </div>
        <div id="footer"><a href="#">Log out</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="anagraphic">
    <h2>Anagraphic data</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 4]">
        <li>
          <div><span class="key">
              <xsl:value-of select="fieldName"/></span>
            <p class="value">
              <xsl:value-of select="content"/>
            </p>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="#">Edit Anagraphic</a>
  </xsl:template>
  <xsl:template match="studyTitles">
    <h2>Study titles</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 4]">
        <li>
          <div><span class="key">Year of attainment</span>
            <p class="value">
              <xsl:value-of select="year"/>
            </p>
          </div>
          <div><span class="key">Title</span>
            <p class="value">
              <xsl:value-of select="title"/>
            </p>
          </div>
          <div><span class="key">School</span>
            <p class="value">
              <xsl:value-of select="school"/>
            </p>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="#">Edit Study Titles</a>
  </xsl:template>
</xsl:stylesheet>