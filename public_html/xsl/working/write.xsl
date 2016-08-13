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
          <p>Admin Panel<a href="home.cgi"> Home</a><span class="active">/ Working Experiences</span>
            <div id="nav">
              <h2>Resume Pages:</h2>
              <ul>
                <li><a href="home.cgi">Overview</a></li>
                <li><a href="anagraphic.cgi">Edit Anagraphical Informations</a></li>
                <li><a href="studyTitles.cgi">Edit Study Titles and Education</a></li>
                <li><span class="active">Edit Working Experience</span></li>
                <li><a href="contacts.cgi">Contacts and Socials</a></li>
              </ul>
            </div>
          </p>
        </div>
        <div id="content">
          <xsl:apply-templates select="working"/>
        </div>
        <div id="footer"><a class="admin" href="logout.cgi">Log out</a>
          <p class="copyright">Copyright (c) 2016 Copyright Holder All Rights Reserved.</p>
        </div>
      </div>
      <script type="text/javascript" src="../../../public_html/javascript/modal.js">//</script>
    </body>
  </xsl:template>
  <xsl:template match="working">
    <div id="modal-div">
      <h2>Proceed with the deletion ?</h2>
      <form class="inline" action="../../actions/destroy.cgi" method="post">
        <fieldset class="inline" id="modal">
          <button type="submit" id="modal-submit">Confirm</button>
        </fieldset>
      </form>
      <button class="inline">
        <xsl:attribute name="onclick">return cancelModal("<xsl:value-of select="@id" />", "working");
</xsl:attribute>Cancel
      </button>
    </div>
    <div>
      <h2 class="page-title">Working Experiences</h2>
      <form class="form" action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="working"/>
          <button type="submit">New Working Experience</button>
        </fieldset>
      </form>
    </div>
    <div class="box-full">
      <ul>
        <xsl:for-each select="item">
          <xsl:sort select="position()" data-type="number" order="descending"/>
          <li>
            <div class="item">
              <p class="titleName">
                <xsl:value-of select="role"></xsl:value-of>
              </p>
              <div><span class="key">From</span><span class="value">
                  <xsl:value-of select="begin"/></span><span class="key">To</span><span class="value">
                  <xsl:value-of select="end"/></span></div>
              <div><span class="key">Company</span>
                <p class="value">
                  <xsl:value-of select="company"></xsl:value-of>
                </p>
              </div>
            </div>
            <form class="form inline-form" action="edit.cgi" method="post">
              <fieldset>
                <input type="hidden" name="collection" value="working"/>
                <input type="hidden" name="id" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="@id" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="begin" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="begin" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="end" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="end" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="role" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="role" />
                  </xsl:attribute>
                </input>
                <input type="hidden" name="company" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="company" />
                  </xsl:attribute>
                </input>
                <button type="submit"> Edit </button>
              </fieldset>
            </form>
            <form class="form inline-form" action="delete.cgi" method="post"><xsl:attribute name="onclick">return renderModal("<xsl:value-of select="@id" />", "working");
</xsl:attribute>
              <fieldset>
                <input type="hidden" name="collection" value="working"/>
                <input type="hidden" name="id" >
                  <xsl:attribute name="value">
                    <xsl:value-of select="@id" />
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