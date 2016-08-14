<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Contacts and Socials - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Contacts and Socials"/>
      <meta name="description" content="Anagraphic Informations of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="Anagraphic Informations, Birth, Address, Giovanni, Rodighiero, Resume, Curriculum Vitae, Experience, Education"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="working">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p><a href="/cgi-bin/pages/public/home.cgi">Home</a><span class="active">/ Contacts and Socials</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="/cgi-bin/pages/public/home.cgi">Overview</a></li>
            <li><a href="anagraphic.cgi">Anagraphical Informations</a></li>
            <li><a href="studyTitles.cgi">Study Titles and Education</a></li>
            <li><a href="studyTitles.cgi">Working Experience</a></li>
            <li><a href="skills.cgi">Skills and Languages</a></li>
            <li><span class="active">Contacts and Socials</span></li>
          </ul>
        </div>
        <div id="content">
          <div class="box-full">
            <xsl:apply-templates select="contacts"/>
          </div>
        </div><a class="back-top" href="#content">Back to top              </a>
        <div id="footer"><a class="admin" href="login.cgi">Admin area</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="contacts">
    <h2 class="page-title">Contacts and Socials</h2>
    <ul>
      <xsl:for-each select="item">
        <li>
          <div class="item">
            <div><span class="key">
                <xsl:value-of select="contactName"></xsl:value-of></span>
              <p class="value">
                <xsl:choose>
                  <xsl:when test="value/@isLink"><a class="external-link">
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
          </div>
        </li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>