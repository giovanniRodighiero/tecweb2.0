<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="//anagraphic">
    <h1>Dati anagrafici
      <form action="edit.cgi" method="POST">
        <label for="item_name">item_name</label>
        <input id="input" type="text" name="item_name"/>
        <label for="input">text</label>
        <input id="item_name" type="text" name="text"/>
        <button type="submit">invia</button>
      </form>
    </h1>
  </xsl:template>
</xsl:stylesheet>