<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="//anagraphic">
    <h1>Dati anagrafici</h1>
    <xsl:for-each select="item"><span>
        <xsl:value-of select="fieldName"/></span>
      <li>
        <xsl:value-of select="content"/>
        <form action="edit.cgi" method="post">
          <fieldset>
            <input type="hidden" name="collection" value="anagraphic"/>
            <input type="hidden" name="id" >
              <xsl:attribute name="value">
                <xsl:value-of select="@idCommento" />
              </xsl:attribute>
            </input>
            <input type="hidden" name="fieldName" >
              <xsl:attribute name="value">
                <xsl:value-of select="fieldName" />
              </xsl:attribute>
            </input>
            <input type="hidden" name="content" >
              <xsl:attribute name="value">
                <xsl:value-of select="content" />
              </xsl:attribute>
            </input>
            <button type="submit"> Modifica </button>
          </fieldset>
        </form>
      </li>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>