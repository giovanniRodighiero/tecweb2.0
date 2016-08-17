<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Study Titles and Education - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Study Titles and Education"/>
      <meta name="description" content="Study Titles and Education of Giovanni Rodighiero."/>
      <meta name="keywords" content="Study Titles, Degree, Education, Diploma,School, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="anagraphic">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p><a href="home.cgi">Home</a><span class="active">/ Study Titles and Education</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="home.cgi" accesskey="o"><span class="accesskey">O</span>verview</a></li>
            <li><a href="anagraphic.cgi" accesskey="a"><span class="accesskey">A</span>nagraphical Informations</a></li>
            <li><span class="active"><span class="accesskey">S</span>tudy Titles and Education</span></li>
            <li><a href="working.cgi" accesskey="w"><span class="accesskey">W</span>orking Experience</a></li>
            <li><a href="skills.cgi" accesskey="k">S<span class="accesskey">k</span>ills and Languages</a></li>
            <li><a href="contacts.cgi" accesskey="c"><span class="accesskey">C</span>ontacts and Socials</a></li>
          </ul>
        </div>
        <div id="content">
          <div class="box-full">
            <xsl:apply-templates select="studyTitles"/>
          </div>
        </div><a class="back-top" href="#content">Back to top</a>
        <div id="footer"><a class="admin" href="login.cgi">Admin area</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="studyTitles">
    <h2 class="page-title">Study Titles and Education</h2>
    <ul>
      <xsl:for-each select="item">
        <xsl:sort select="position()" data-type="number" order="descending"/>
        <li>
          <div class="studyTitle">
            <p class="titleName">
              <xsl:value-of select="title"/>
            </p>
            <div><span class="key">Year of attainment</span>
              <p class="value">
                <xsl:value-of select="year"/>
              </p>
            </div>
            <div><span class="key">School</span>
              <p class="value">
                <xsl:value-of select="school"/>
              </p>
            </div>
          </div>
        </li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>