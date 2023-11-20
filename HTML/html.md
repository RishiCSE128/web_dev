# HTML Basics

## Quotation
### Block Quotations
* The HTML `<blockquote>` element defines a section that is quoted from another source.
* Browsers usually indent `<blockquote>` elements.

Example:
```html
<p>Here is a quote from WWF's website:</p>

<blockquote cite="http://www.worldwildlife.org/who/index.html">

For 60 years, WWF has worked to help people and nature thrive. As the world's leading conservation organization, WWF works in nearly 100 countries. At every level, we collaborate with people around the world to develop and deliver innovative solutions that protect communities, wildlife, and the places in which they live.

</blockquote>
```

<p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 60 years, WWF has worked to help people and nature thrive. As the world's leading conservation organization, WWF works in nearly 100 countries. At every level, we collaborate with people around the world to develop and deliver innovative solutions that protect communities, wildlife, and the places in which they live.
</blockquote>

### Short Quotation
* The HTML `<q>` tag defines a short quotation.
* Browsers normally insert quotation marks around the quotation.

Example:
```html
<p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>
```
<p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>

### Abbreviations
*The HTML `<abbr>` tag defines an abbreviation or an acronym, like "HTML", "CSS", "Mr.", "Dr.", "ASAP", "ATM".
* Marking abbreviations can give useful information to browsers, translation systems and search-engines.
* Tip: Use the global title attribute to show the description for the abbreviation/acronym when you mouse over the element. 

Example:
```html
<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>
```

<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>

### Address & Contact Information
* The HTML `<address>` tag defines the contact information for the author/owner of a document or an article.
* The contact information can be an email address, URL, physical address, phone number, social media handle, etc.
* The text in the `<address>` element usually renders in italic, and browsers will always add a line break before and after the `<address>` element.

Example:
```html
<address>
Written by John Doe.<br>
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```
<address>
Written by John Doe.<br>
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>


### Citation 
* The HTML <cite> tag defines the title of a creative work (e.g. a book, a poem, a song, a movie, a painting, a sculpture, etc.).
* Note: A person's name is not the title of a work.
* The text in the <cite> element usually renders in italic.

Example
```html
<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>
```
<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>

### Bi-Directional Override
* BDO stands for Bi-Directional Override.
* The HTML `<bdo>` tag is used to override the current text direction:

Example:
```html
<bdo dir="rtl">This text will be written from right to left</bdo>
```
<bdo dir="rtl">This text will be written from right to left</bdo>

## Comments 
HTML comments are not displayed in the browser, but they can help document your HTML source code.

You can add comments to your HTML source by using the following syntax:
```html
<!-- Write your comments here -->
```
## Colors
HTML colors are specified with predefined color names, or with RGB, HEX, HSL, RGBA, or HSLA values.
### Background Color
You can set the background color for HTML elements:

Example:
```html
<h1 style="background-color:DodgerBlue;">Hello World</h1>
<p style="background-color:Tomato;">Lorem ipsum...</p>
```
<h1 style="background-color:DodgerBlue;">Hello World</h1>
<p style="background-color:Tomato;">Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat.</p>

### Text Color
You can set the color of text:

Example:
```html
<h1 style="color:Tomato;">Hello World</h1>
<p style="color:DodgerBlue;">Lorem ipsum...</p>
<p style="color:MediumSeaGreen;">Ut wisi enim...</p>
```
<h1 style="color:Tomato;">Hello World</h1>
<p style="color:DodgerBlue;">Lorem ipsum...</p>
<p style="color:MediumSeaGreen;">Ut wisi enim...</p>

### Border Color
You can set the color of borders

Example
```html
<h1 style="border:2px solid Tomato;">Hello World</h1>
<h1 style="border:2px solid DodgerBlue;">Hello World</h1>
<h1 style="border:2px solid Violet;">Hello World</h1>
```
<h1 style="border:2px solid Tomato;">Hello World</h1>
<h1 style="border:2px solid DodgerBlue;">Hello World</h1>
<h1 style="border:2px solid Violet;">Hello World</h1>

### Color Values
* In HTML, colors can also be specified using RGB values, HEX values, HSL values, RGBA values, and HSLA values.
* The following three `<div>` elements have their background color set with RGB, HEX, and HSL values

Example:
```html
<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>
```
<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>