# MicroPythonScripts

Repository for MicroPython scripts for different applications.

## Structure for the Repository

```
Main Repository Folder(MicroPythonScripts)
        └── Script Folders
        |        |
        |        ├── Code
        |        |    └── Commented code
        |        ├── Release
        |        |    └── Uncomment Code
        |        ├── Doc
        |        └── README
        └── HelpScript Folder
            |
            ├── MicroPythonModules Folder
            |     ├── Code
            |     |    └── Commented code
            |     ├── Release
            |     |    └── Uncomment Code
            |     ├── Doc
            |     └── Examples
            |     └── README
            ├── PythonScripts Folder
            |     ├── Code
            |     |    └── Commented code
            |     └── README
            ├── HTML
            └── CSS
```
___
## **Script Folder**
  Folder containing everything related to the script.
  * ### Code Folder
  Commented code for better understanding of it.
  * ### Release Folder
  Code without comments and trying to be as small as possible in order to save memory on the microcontroller.
  * ### Doc Folder
  Folder containing the files like images and so on for documentation purposes.
___
## **HelpScript Folder**
Folder containing everything related to MicroPython and some help classes and scripts to make deployments more easy.
  * ### Code Folder
  Commented code for better understanding of it.
  * ### Release Folder
  Code without comment and trying to be as small as possible in order to save memory on the microcontroller.
  * ### Doc Folder
  Folder containing the files like images and so on for documentation purposes.
  * ### Example Folder
  Folder containing the example files that in some cases will need to be renamed into `main.py` so it will be run at boot time.

**NOTE:** Some of the code on this `HelpScript` folder might be commented and it would take more space than required on the board.
___
### **README files on folders**
Documentation of the script, class or other important information.
