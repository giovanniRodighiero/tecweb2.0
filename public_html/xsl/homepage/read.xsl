<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>HomePage - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - HomePage"/>
      <meta name="description" content="HomePage of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="Giovanni, Rodighiero, Resume, Curriculum Vitae, Experience, Education"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="homepage">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero</span>  Resume</h1>
        </div>
        <div id="path">
          <p>Home</p>
        </div>
        <div id="nav">
          <ul>
            <li><a href="/cgi-bin/pages/public/anagraphic.cgi">Anagraphic</a></li>
            <li><a href="#">Study Titles</a></li>
            <li><a href="#">Working Experience</a></li>
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
        <div id="footer"><a href="login.cgi">Admin area</a>
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
    </ul><a href="#">Show all</a>
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
    </ul><a href="#">Show all</a>
  </xsl:template>
</xsl:stylesheet>