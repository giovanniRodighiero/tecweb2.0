<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>HomePage Admin - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Admin HomePage"/>
      <meta name="description" content="Admin homepage of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="Giovanni, Rodighiero, Resume, Curriculum Vitae, Experience, Education, Skills, Contacts, Socials"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="homepage">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div><a class="skipMenu" href="#content">Jump to the page content</a>
        <div id="path">
          <p>Admin Panel<span class="active">Home</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><span class="active"><span class="accesskey">O</span>verview</span></li>
            <li><a href="anagraphic.cgi" accesskey="a">Edit <span class="accesskey">A</span>nagraphical Informations</a></li>
            <li><a href="studyTitles.cgi" accesskey="s">Edit <span class="accesskey">S</span>tudy Titles and Educations</a></li>
            <li><a href="working.cgi" accesskey="w">Edit <span class="accesskey">W</span>orking Experience</a></li>
            <li><a href="skills.cgi" accesskey="k">Edit S<span class="accesskey">k</span>ills and Languages</a></li>
            <li><a href="contacts.cgi" accesskey="c">Edit <span class="accesskey">C</span>ontacts and Socials</a></li>
          </ul>
        </div>
        <div id="content">
          <div class="image"><img src="../../../images/photo.png" alt="Picture of Giovanni Rodighiero"/></div>
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
        </div><a class="back-top" href="#content">Back to top</a>
        <div id="footer"><a class="admin" href="logout.cgi">Log out</a>
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
          <div><span class="key">
              <xsl:value-of select="fieldName"/></span>
            <p class="value">
              <xsl:value-of select="content"/>
            </p>
          </div>
        </li>
      </xsl:for-each>
    </ul><a href="anagraphic.cgi">Edit Anagraphical Informations</a>
  </xsl:template>
  <xsl:template match="studyTitles">
    <h2>Study Titles and Educations</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 2]">
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
    </ul><a href="studyTitles.cgi">Edit Study Titles and Educations</a>
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
    </ul><a href="working.cgi">Edit Working Experiences</a>
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
    </ul><a href="skills.cgi">Edit Skills and Languages</a>
  </xsl:template>
  <xsl:template match="contacts">
    <h2>Contacts and Socials</h2>
    <ul>
      <xsl:for-each select="item[position() &lt; 3]">
        <li>
          <div class="contacts"><span class="key">
              <xsl:value-of select="contactName"/></span>
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
        </li>
      </xsl:for-each>
    </ul><a href="contacts.cgi">Edit Contacts and Socials</a>
  </xsl:template>
</xsl:stylesheet>