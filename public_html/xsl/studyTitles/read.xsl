<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="studyTitles">
    <h1>Study titles</h1>
    <ul>
      <xsl:for-each select="item">
        <li>
          <div><strong>Year</strong><span>
              <xsl:value-of select="year"/></span></div>
          <div><strong>Title</strong><span>
              <xsl:value-of select="title"/></span></div>
          <div><strong>School</strong><span>
              <xsl:value-of select="school"/></span></div>
        </li>
      </xsl:for-each>
    </ul>
  </xsl:template>
</xsl:stylesheet>