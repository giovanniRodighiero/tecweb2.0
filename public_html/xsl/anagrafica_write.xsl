<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="//anagrafica">
    <h1>Dati anagrafici
      <form action="edit.cgi" method="POST">
        <label for="input">input</label>
        <input id="input" type="text" name="test"/>
        <button type="submit">invia</button>
      </form>
    </h1>
  </xsl:template>
</xsl:stylesheet>