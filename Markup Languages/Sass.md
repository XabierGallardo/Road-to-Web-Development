# SASS / Syntactically Awesome Stylesheets
Sass extends CSS with more features, from not repeating yourself.
It provides a compiler that allows us to write stylesheed in a different language, from the **.sass** file removes the semicolons and curly braces to the most popular **.scss** that can be written like regular css and then it's extended with bonus features.

When we finish writting the code, the compiler takes our code and convert it into valid css that can run in a browser.

#### Variables
Variables allows us to reference a value everywhere
```scss
$red: hsl(0, 100%, 50%);

.button.danger { 
	color: $red;
	border: 1px solid $red;
}
```

#### Nesting
Instead of duplicating name spaces, we can nest styles inside the parent

From
```css
.button a { font-weight: bold; }

.button.danger { color:red; }
```

To
```scss
.button {
	a { 
		font-weight: bold;
	}

	.success {
		color: green
	}
}
```

#### Ampersand
To refer to the parent selector, we use **&**, so instead of doing
```css
.btn:focus { }
.btn:hover { }
.btn:active { }
```

We can apply changes to a direct slibing
```scss
.btn {
	&:focus { }
	&:hover { }
	&:active { }
}
```

#### Mixing
To avoid using the same group of styles, like
```css
.card {
	display: flex;
	flex-direction: column;
	background: gray;
}
.aside {
	display: flex;
	flex-direction: column;
	background: gray;
}
```

We can encapsulate a group of styles and then apply those styles anywhere using the **include** keyword
```scss
@mixin flex-column {
	display: flex;
	flex-direction: column;
	background: gray;
}

.card {
	@include flex-column;
}

.aside {
	@include flex-column;
}
```

Mixins can even take arguments to create a large number of similar classes
```scss
@mixin cool-button($color, $bg) {
	display: flex;
	color: $color;
	background: $bg;
}

.btn-orange {
	@include cool-button(black, orange);
}
```

#### Functions
Sass provides a whole suit of tools to help with more programmatic code

From reusable code
```scss
@function sum($numbers) {
	$sum: 0;

	@each $number in $numbers {
		$sum: $sum + $number;
	}

	@return $sum;
}
```

To already built-in functions
```scss
$base-color: green;

.card {
	background: lighten($base-color, 25%);
	background: darken($base-color, 25%);
}
```
