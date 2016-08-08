<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="studyTitles">
    <h1>Study Titles</h1>
    <div>
      <form action="new.cgi" method="post">
        <fieldset>
          <input type="hidden" name="collection" value="studyTitles"/>
          <button type="submit">New title</button>
        </fieldset>
      </form>
    </div>
    <ul>
      <xsl:for-each select="item">
        <li>
          <div><strong>Year</strong><span>
              <xsl:value-of select="year"/></span></div>
          <div><strong>Title</strong><span>
              <xsl:value-of select="title"/></span></div>
          <div><strong>School</strong><span>
              <xsl:value-of select="school"/></span></div>
          <form action="edit.cgi" method="post">
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
          <form action="delete.cgi" method="post">
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