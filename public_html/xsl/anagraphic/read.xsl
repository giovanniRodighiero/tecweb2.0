<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="anagraphic">
    <h1>Dati anagrafici</h1>
    <ul>
      <xsl:for-each select="item"><span>
          <xsl:value-of select="fieldName"/></span>
        <li>
          <xsl:value-of select="content"/>
        </li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>