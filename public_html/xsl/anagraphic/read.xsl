<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="//anagraphic">
    <h1>Dati anagrafici</h1>
    <ul>
      <xsl:for-each select="item">
        <li><span>
            <xsl:value-of select="fieldName"/></span><span>
            <xsl:value-of select="content"/></span></li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>