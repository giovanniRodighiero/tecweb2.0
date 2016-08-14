<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Skills and Languages Admin - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Skills and Languages"/>
      <meta name="description" content="Skills and Languages knows and possessed by Giovanni Rodighiero."/>
      <meta name="keywords" content="Skills, Languages, Technologies, level, Giovanni, Rodighiero, Resume, Curriculum Vitae"/>
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
          <p>Admin Panel<a href="home.cgi"> Home</a><span class="active">/ Skills and Languages</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="home.cgi" accesskey="o"><span class="accesskey">O</span>verview</a></li>
            <li><a href="anagraphic.cgi" accesskey="a">Edit <span class="accesskey">A</span>nagraphical Informations</a></li>
            <li><a href="studyTitles.cgi" accesskey="s">Edit <span class="accesskey">S</span>tudy Titles and Educations</a></li>
            <li><a href="working.cgi" accesskey="w">Edit<span class="accesskey">W</span>orking Experience</a></li>
            <li><span class="active">Edit <span class="accesskey">S</span>kills and Languages</span></li>
            <li><a href="contacts.cgi" accesskey="c">Edit <span class="accesskey">C</span>ontacts and Socials</a></li>
          </ul>
        </div>
        <div id="content">
          <xsl:apply-templates select="skills"/>
        </div><a class="back-top" href="#content">Back to top</a>
        <div id="footer"><a class="admin" href="logout.cgi">Log out</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
      <script type="text/javascript" src="../../../public_html/javascript/modal.js">//</script>
    </body>
  </xsl:template>
  <xsl:template match="skills">
    <div id="modal-div">
      <h2>Proceed with the deletion ?</h2>
      <form class="inline" action="../../actions/destroy.cgi" method="post">
        <fieldset class="inline" id="modal">
          <button type="submit" id="modal-submit">Confirm</button>
        </fieldset>
      </form>
      <button class="inline">
        <xsl:attribute name="onclick">return cancelModal("<xsl:value-of select="@id" />", "skills");
</xsl:attribute>Cancel
      </button>
    </div>
    <div>
      <h2 class="page-title">Skills and Languages</h2>
      <form class="form" action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="skills"/>
          <button type="submit">New Skill</button>
        </fieldset>
      </form>
    </div>
    <div class="box-full">
      <ul>
        <xsl:for-each select="item">
          <li>
            <div class="item">
              <p class="titleName">
                <xsl:value-of select="skillsName"/>
              </p>
              <div><span class="key">Level of Knowledge</span><span class="value">
                  <xsl:value-of select="level"/></span></div>
            </div>
            <form class="form inline-form" action="edit.cgi" method="post">
              <fieldset>
                <input type="hidden" name="collection" value="skills"/>
                <input type="hidden" name="id" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="@id" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="skillsName" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="skillsName" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="level" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="level" />
                  </xsl:attribute>
                </input>
                <button type="submit"> Edit </button>
              </fieldset>
            </form>
            <form class="form inline-form" action="delete.cgi" method="post"><xsl:attribute name="onclick">return renderModal("<xsl:value-of select="@id" />", "skills");
</xsl:attribute>
              <fieldset>
                <input type="hidden" name="collection" value="skills"/>
                <input type="hidden" name="id" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="@id" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="skillsName" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="skillsName" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="level" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="level" />
                  </xsl:attribute>
                </input>
                <button type="submit"> Delete </button>
              </fieldset>
            </form>
          </li>
        </xsl:for-each>
      </ul>
    </div>
  </xsl:template>
</xsl:stylesheet>