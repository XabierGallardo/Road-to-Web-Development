# Visual Studio Config & Basics


## HTML
**Emmet Feature**: Creates the whole html basic template
```sh
# Write
html
# Click on html:5
```


## [Markdown](http://www.freecodecamp.org/news/markdown-cheat-sheet/)
Download **Auto-Open Markdown Preview** Extension


## Auto Format / Indentation
Keyboard Shortcut to manual indentation
Select the text to fix with the keyboard or cursor
**Alt + Shift + F**

Instead of doing manual indentation, we can automate this process
1. Config -> Settings
2. Text Editor -> Formatting
3. Select Format On Paste to automatically format the pasted content
4. Select Format On Save to automatically format the code everytime we type *Ctrl+S* or File -> Save

Another option for languages that don't have a native support from visual studio is using Extensions like **Prettier** and **Linter**


## SSH Connection
We can use Visual Studio Code on our server using the **Remote -SSH** Extension
File -> Preferences -> Extensions
Write *Remote - SSH* from Microsoft and Install it

##### Getting started
1. Press F1 and run the **Remote-SSH: Open SSH Host**
2. Write the ssh command *ssh example@192.168.1.10*
3. After we add it, we'll connect to that direction and a new window pop up asking for the password
4. Once we're connected we'll have our terminal on the bottom of the screen and we can access any folder on File -> Open Folder

That's it! Now simply using **F1** we'll have a shortcut to access our server!


## Themes
My favourite one is Dracula theme
https://draculatheme.com/visual-studio-code/

1. View -> Command Pallette
2. Write Install Extension and Enter
3. Write Dracula Official and Enter