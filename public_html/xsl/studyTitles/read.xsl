<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Anagraphic Informations - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Anagraphic Informations"/>
      <meta name="description" content="Anagraphic Informations of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="Anagraphic Informations, Birth, Address, Giovanni, Rodighiero, Resume, Curriculum Vitae, Experience, Education"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="anagraphic">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p><a href="/cgi-bin/pages/public/home.cgi">Home</a><span class="active">/ Study Titles and Education</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="home.cgi">Overview</a></li>
            <li><a href="anagraphic.cgi">Anagraphical Informations</a></li>
            <li><span class="active">Study Titles and Education</span></li>
            <li><a href="working.cgi">Working Experience</a></li>
            <li><a href="skills.cgi">Skills and Languages</a></li>
            <li><a href="contacts.cgi">Contacts and Socials</a></li>
          </ul>
        </div>
        <div id="content">
          <div class="box-full">
            <xsl:apply-templates select="studyTitles"/>
          </div>
        </div>
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