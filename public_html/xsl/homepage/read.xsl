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
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p><span class="active">Home</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><span class="active">Overview</span></li>
            <li><a href="anagraphic.cgi">Anagraphical Informations</a></li>
            <li><a href="studyTitles.cgi">Study Titles and Education</a></li>
            <li><a href="working.cgi">Working Experience</a></li>
            <li><a href="skills.cgi">Skills and Languages</a></li>
            <li><a href="contacts.cgi">Contacts and Socials</a></li>
          </ul>
        </div>
        <div id="content">
          <div class="image"><img src="../../../public_html/images/photo.png"/></div>
          <div class="box right-box">
            <xsl:apply-templates select="anagraphic"/>
          </div>
          <div class="box">
            <xsl:apply-templates select="studyTitles"/>
          </div>
          <div class="box">
            <xsl:apply-templates select="working"/>
          </div>
          <div class="box">
            <xsl:apply-templates select="skills"/>
          </div>
          <div class="box">
            <xsl:apply-templates select="contacts"/>
          </div>
        </div>
        <div id="footer"><a class="admin" href="login.cgi">Admin area</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
    </body>
  </xsl:template>
  <xsl:template match="anagraphic">
    <h2>Anagraphical Informations</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 6]">
        <li>
          <div class="item"><span class="key">
              <xsl:value-of select="fieldName"/></span>
            <p class="value">
              <xsl:value-of select="content"/>
            </p>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="/cgi-bin/pages/public/anagraphic.cgi">Show all</a>
  </xsl:template>
  <xsl:template match="studyTitles">
    <h2>Study titles and Education</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 4]">
        <xsl:sort select="position()" data-type="number" order="descending"/>
        <li>
          <div class="studyTitle">
            <p class="titleName">
              <xsl:value-of select="title"/>
            </p>
            <div class="infos">
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
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="studyTitles.cgi">Show all</a>
  </xsl:template>
  <xsl:template match="working">
    <h2>Working Experience</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 2]">
        <xsl:sort select="position()" data-type="number" order="descending"/>
        <li>
          <div class="working">
            <p class="titleName">
              <xsl:value-of select="role"/>
            </p>
            <div class="infos">
              <div><span class="key">From</span>
                <p class="value">
                  <xsl:value-of select="begin"/>
                </p><span class="key">To</span>
                <p class="value">
                  <xsl:value-of select="end"/>
                </p>
              </div>
              <div><span class="key">For</span>
                <p class="value">
                  <xsl:value-of select="company"/>
                </p>
              </div>
            </div>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="working.cgi">Show All</a>
  </xsl:template>
  <xsl:template match="skills">
    <h2>Skills and Languages</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 4]">
        <li>
          <div class="item"><span class="key">
              <xsl:value-of select="skillsName"/></span>
            <p class="value">
              <xsl:value-of select="level"/>
            </p>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="skills.cgi">Show all</a>
  </xsl:template>
  <xsl:template match="contacts">
    <h2>Contacts and Socials</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 3]">
        <li>
          <div class="contacts"><span class="key">
              <xsl:value-of select="contactName"/>
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
              </p></span></div>
        </li>
      </xsl:for-each>
    </ul><a href="contacts.cgi">Show All</a>
  </xsl:template>
</xsl:stylesheet>