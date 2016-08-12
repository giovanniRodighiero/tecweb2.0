<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output version="1.0" encoding="UTF-8" indent="yes" omit-xml-declaration="yes"/>
  <xsl:template match="//db">
    <head>
      <title>Anagraphic Informations Admin - Giovanni Rodighiero Resume</title>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <meta name="title" content="Giovanni Rodighiero Resume - Anagraphic Informations"/>
      <meta name="description" content="Anagraphic Informations admin panel of the website that presents Giovanni Rodighiero's resume."/>
      <meta name="keywords" content="Anagraphic Informations,Admin, Birth, Address, Giovanni, Rodighiero, Resume, Curriculum Vitae, Experience, Education"/>
      <meta name="author" content="Giovanni Rodighiero"/>
      <meta name="language" content="english en"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/main.min.css" media="screen"/>
      <link rel="stylesheet" type="text/css" href="../../../public_html/styles/print.min.css" media="print"/>
    </head>
    <body>
      <div id="homepage">
        <div id="header">
          <h1><span xml:lang="it">Giovanni Rodighiero,</span><span class="subtitle">Personal Resume</span></h1>
        </div>
        <div id="path">
          <p>Admin Panel<a href="home.cgi"> Home</a><span class="active">/ Study Titles and Education</span></p>
        </div>
        <div id="nav">
          <h2>Resume Pages:</h2>
          <ul>
            <li><a href="home.cgi">Overview</a></li>
            <li><a href="anagraphic.cgi">Edit Anagraphical Informations</a></li>
            <li class="active">Edit Study Titles and Educations</li>
            <li><a href="#">Edit Working Experience</a></li>
          </ul>
        </div>
        <div id="content">
          <div class="box-full">
            <xsl:apply-templates select="studyTitles"/>
          </div>
        </div>
        <div id="footer"><a class="admin" href="logout.cgi">Log out</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
      <script type="text/javascript" src="../../../public_html/javascript/modal.js">//</script>
    </body>
  </xsl:template>
  <xsl:template match="studyTitles">
    <div id="modal-div">
      <h2>Proceed with the deletion ?</h2>
      <form class="inline" action="../../actions/destroy.cgi" method="post">
        <fieldset class="inline" id="modal">
          <button type="submit" id="modal-submit">Confirm</button>
        </fieldset>
      </form>
      <button class="inline">
        <xsl:attribute name="onclick">return cancelModal("<xsl:value-of select="@id" />", "studyTitles");
</xsl:attribute>Cancel
      </button>
    </div>
    <div>
      <h2 class="page-title">Study Titles and Education</h2>
      <form class="form" action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="studyTitles"/>
          <button type="submit">New title</button>
        </fieldset>
      </form>
    </div>
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
          <form class="form inline-form" action="edit.cgi" method="post">
            <fieldset>
              <input type="hidden" name="collection" value="studyTitles"/>
              <input type="hidden" name="id" >
                <xsl:attribute name="value">
                  <xsl:value-of select="@id" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="year" >
                <xsl:attribute name="value">
                  <xsl:value-of select="year" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="title" >
                <xsl:attribute name="value">
                  <xsl:value-of select="title" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="school" >
                <xsl:attribute name="value">
                  <xsl:value-of select="school" />
                </xsl:attribute>
              </input>
              <button type="submit"> Edit </button>
            </fieldset>
          </form>
          <form class="form inline-form" action="delete.cgi" method="post"><xsl:attribute name="onclick">return renderModal("<xsl:value-of select="@id" />", "studyTitles");
</xsl:attribute>
            <fieldset>
              <input type="hidden" name="collection" value="studyTitles"/>
              <input type="hidden" name="id" >
                <xsl:attribute name="value">
                  <xsl:value-of select="@id" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="year" >
                <xsl:attribute name="value">
                  <xsl:value-of select="year" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="title" >
                <xsl:attribute name="value">
                  <xsl:value-of select="title" />
                </xsl:attribute>
              </input>
              <input type="hidden" name="school" >
                <xsl:attribute name="value">
                  <xsl:value-of select="school" />
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