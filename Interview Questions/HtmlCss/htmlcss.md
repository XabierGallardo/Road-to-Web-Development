# HTML & CSS Interview Questions


# HTML
#### 1 - HTML
You are working on this webpage where you want to add this section called Developers, and when clicked on it, it should show your name. How will you do that?

```sh
# 1
<section>
	<details>Developers</details>
	Mr.XYZ
</section>

# 2
<details>
	<summary>Developers</summary>
	Mr.XYZ
</details>

# 3
<summary>
	<details>Developers</details>
	Mr.XYZ
</summary>

# 4
<details>
	Developers Mr.XYZ
</details>
```


#### 2 - HTML
You are working on an incomplete piece of code on a webpage
```sh
<ABC>
	<img src="img.jpg" alt="image">
	<XYZ>Fig1. Image1</XYZ>
</ABC>
```
Which tags should be used instad of ABC and XYZ?

- image and figcaption
- img and caption
- figure and figcaption
- fig and caption


#### 3 - HTML
Which type of content-type is correct for the script header sent from the server for SSE in HTML5?

- text/application-stream
- text/data-stream
- text/event-stream
- None of the mentioned


#### 4 - HTML
You are working on an HTML5 application that has a cloud file storage option.
You need to support drag and drop operations on the pages.
You want to understand the desired drag operation when the user perfoms dragging.
Using which property can we identify this?

- dropEffect
- dragEnd
- captureData
- getData


#### 5 - HTML
You are working on an application that uses the IndexedDB storage for storing the client-side data.
You need to upgrade the local database version to the new version.
Which is the correct code to achieve the same?

```sh
# 1
var dbRequest = window.indexedDB.open("DBName", 2);

dbRequest.onversionchange = function (evt) {
	if(evt.oldVersion < 1) {
		//create objects for version 1
	}
	//other version upgrade paths
}

# 2
var dbRequest = window.indexedDB.open("DBName", 2);

dbRequest.ondatabaseupgrade = function (evt) {
	if(evt.oldVersion < 1) {
		//create objects for version 1
	}
	//other version upgrade paths
}

# 3
var dbRequest = window.indexedDB.open("DBName", 2);

dbRequest.onupgradeneeded = function (evt) {
	if(evt.oldVersion < 1) {
		//create objects for version 1
	}
	//other version upgrade paths
}

# 4
var dbRequest = window.indexedDB.open("DBName", 2);

dbRequest.onupgrade = function (evt) {
	if(evt.oldVersion < 1) {
		//create objects for version 1
	}
	//other version upgrade paths
}
```


# CSS
#### 1 - CSS
In a given scenario where you need to show the items with class "reverse" in reverse order for devices with a width of less than 400px, which of the following snippets will you add to the CSS file?


```sh
# 1
@media (min-width: 400px) {
	.reverse{
		flex-direction: row-reverse;
	}
}

# 2
@media (max-width: 400px) {
	.reverse{
		flex-direction: row-reverse;
	}
}

# 3
@media {
	.reverse{
		flex-direction: row-reverse;
	}
}

# 4
.reverse{
	flex-direction: row-reverse;
}
```


#### 2 - CSS
Which of the following four values work on border-radius?

- top, bottom, left, right
- up, down, front, behind
- top-left, top-right, bottom-left, bottom-right
- bottom-left, bottom0right, top-right, top-left


#### 3 - CSS
You are working on this webpage where you want to show a car image moving back and forth continuously
Which of the following option canbe used for the same?

- Create an animation that moves the image from, say left to right and then set the animation direction to alternate and the animation iteration count to infinite
- Create an animation that moves the image from, say left to right and then set the animation direction to reverse and the animation interation count to infinite
- Create an animation that moves the image from, say, left to right and then set the animation direction to alternate and the animation duration to infinite
- None of these


#### 4 - CSS
You need to set margins of certain images using the CSS float property.
In order to do so, you select images that have a style property of float set to the left and set their left and bottom margins to 5 px and 15 px respectively.

Which of the following CSS rules can be used to achieve this objective?

```sh
# 1
img[style~="float:left"] {
	margin: 0px 0px 5px 15px;
}

# 2
img[style~="float:left"] {
	margin: 5px 15px 0px 0px;
}

# 3
img[style~="float:left"] {
	margin: 5px 15px 0px 0px;
}

# 4
img[style*="float:left"] {
	margin: 5px 15px 0px 0px;
}
```


#### 5 - CSS
You want to use the "begins with" selector provided in the Substring Matching Attribute Selectors of CSS3.
In the given context, select the appropiate way to achieve that.

```sh
# 1
[att^=val]

# 2
[att$=val]

# 3
[att*=val]

# 4
[att%=val]
```