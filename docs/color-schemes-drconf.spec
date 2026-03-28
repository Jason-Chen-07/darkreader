This _small_ document outlines the specification of `src/config/color-schemes.drconf`,
which doesn't really follow the standard used by the other files.

Spec:
- A section is a uniquely defined color scheme following the syntax rules.
- The file must begin with a section named "Default", which has both a light and a dark variant.
- A separator must be placed between sections. The separator is `'='.repeat(32)`.
- A new line must be placed before and after the separator.
- All sections except the first should start with a new line (this is the same new line after the separator).
- The first keyword in the section (after the possible new line) should be a unique color scheme name.
- After 2 new lines following the first keyword, there should be either "DARK" or "LIGHT". At least 1 variant should be defined.
- If a color scheme has both variants, the order should start with "DARK" and then "LIGHT" for consistency.
- Within the variants, a background color and text color can be defined; both are required.
- The syntax for defining background and text colors should be `{background,text}: #6-or-3-length-hex-color`, each on a new line.
- The order should start with background and then text for consistency.
- The parser will return only the first error found, not all of them.
- The file always ends with a new line.


Example:
```txt
Default

DARK
background: #181a1b
text: #e8e6e3

LIGHT
background: #181a1b
text: #e8e6e3

================================

Dracula

DARK
background: #282b36

================================

Nord

DARK
background: #2e3440
text: #eceff4

LIGHT
background: #eceff4
text: #3b4252
