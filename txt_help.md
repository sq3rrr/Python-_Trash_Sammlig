# Hilfe . txt
---

### SDL bugs on Kali Linux


#### Display resolution bug
##### Problem: 

After starting sdl via cmd cd SilentDragonLite ./SilentDragonLite <br/ >
or mouseclick in files, SDL runs but doesnt display the full programwindow, `visible:`<br/> Terms of service <br/ >
Create passphrase<br/><br/>`not visible`:<br/>buttons which are on the bottom left like "Import Seed" <br/>or "New Wallet" even with the VM using the whole screen.

##### Solve:
Change the resolution of your screen, now the y-axis from the screen is too small to display the whole SDL program we need to make it bigger, <br/ >
go in the linux cmd promt. Open cmd and type xrandr, then type xrandr -s 7, 7 will be a format which was displayed before, chose a range between 1900:1300.
The y axis should be over 1200

#### Mouse click bug
##### Prolem:
When creating a new wallet --> SDL doesnt let you click the button "New wallet" on the bottom right side the button is bugged. "Back" and "Cancel" are working.

##### Solve:
click first on the left side "Import Seed/Wallet", then un-accept terms of use, re-accept and now you should be able to click the "New Wallet" Button

#### Sietch transaction display bug in SDL GUI:
##### Problem:
After sending a transaction when you instantly go to "Transactions" and look up your last tx sent: there will be displayed a wrong addr which could cause insecurity <br/ >
or inner pain because you think you sent to wrong address and funds went lost. <br/ >
##### First it will look like this:

|`TypeOfTx` | _Addr_      |    Amount of funds |
| --- | :--- | --- |
| -------------- | ---------------------------- | ---------------------- |
|`Send`      | **zs1SietchTXfirst**     | 50 Hush |
|--------------|----------------------------|----------------------|
|`Receive `  | zs1YourAddr        | 250 Hush |

##### After like 10 to 30 seconds it should fetch the real transaction into the GUI:
|`TypeOfTx` | _Addr_      |    Amount of funds |
| --- | :--- | --- |
| -------------- | ---------------------------- | ---------------------- |
|`Send`      | **zs1YourRealTransaction**     | 50 Hush |
|--------------|----------------------------|----------------------|
|`Receive `  | zs1YourAddr        | 250 Hush |

##### Solve:
No answer for this problem yet.
> According to Duke it is because of Sietch and a GUI (Graphical User Interface); <br/ >
> Before the real (your) transaction gets into a block, the SDL GUI displays one of multiple (up to 9) decoy transaction from Sietch first to fill the space in the "address" folder. <br/ >
> After approx. 30sec the real tx gets into a block and the GUI fetches the real addr into the folder.

---


### Compile SDL (SilentDragonLite) manual for windows-users who want to hide their SDL and HushChat on their PC via VM (Virtual machine)


* install virtualbox like in the manuals for VM
* We need to manually download all compiler packages for linux to install/compile SDL -->
* We need: qtcreator , libqt5websockets5-dev , qt5-qmake, Git, Rust and PowerShell

#### occured problems:
##### Outdated clients as suggested downloads.
For our first compile try we need only :qtcreator , libqt5websockets5-dev , qt5-qmake <br/ >
<br/ >
Outdated clients: qt5-default <> The problem with this package is that the download link, which is integrated  <br/ >
in the installingpackges for linux is no longer active, to solve this problem we ignore the qt5-default package and use qtcreator,qt5make,libqt5websockets5-dev <br/ > <br/ >
Error reports and mistakes while compiling with qt5-default: because the package is outdated the linux cmd promt displays a message that the download is not full or that the package is lacking information or something like that <br/ >
Fatal error during changing the download link for qt5 via wget command --> forgot to install qt5maker and libqt5websockets5-dev, Error displays in cmd say: Theres no such file for qt5maker, another Error: for websockets5 something not found, these error say that something  is missing, so we need to download these also via cmd sudo apt-get install
<br/ > 
start with QT5, QT5 has no 
<br/ >
<br/ >

---
### How to extract password/passphrases and metadata from old WLAN-connections using CMD


#### for windows: 
* ⊞(windows key) + r - opens a search window , then type cmd
* let the computer open the terminal :C:\users\user>    <>
* type: netsh
* type: wlan show profile - opens all ever connected WLAN profiles on your PC
* chose the WLAN you want to extract the Metadata from
* type: wlan show profile "WLAN name" key=clear - Displays all metadata from the WLAN
* so if you re ever sleeping over at a friends and have access to their guest PC/account on PC and forgot their password,
##### use this tool to get your passphrase & log into the WLAN

#### Python trash cmd to display it on your python shell if you are lazy:
```Python
import time

def printthismofomanual():
    somemanuals = {'1.)': '1.) press windows button ⊞ +r',
                   '2.)': '2.) type in: cmd',
                   '3.)': '3.) when <terminal> opens, type inside the <terminal>: netsh',
                   '4.)': '4.) type in <terminal>: wlan show profile',
                   '5.)': '5.) type in <terminal>: wlan show profile "WLAN name numbers" key=clear',
                   'addinfo': '6.) If the WLANname has spaces in between(For example: "TestWLAN 321")\n,just use this format, type in <terminal>: wlan show profile "testwlan 1234 pundestreet bahamas" key=clear'}
    a=[]
    for value in somemanuals.values():
        a.append(value)
    print("Extracting values from keys. . .")
    time.sleep(5)
    print("All values extracted. . .")
    time.sleep(1)
    print("Here is the manual: ")
    return a

#Print out the whole thing with this:
b = printthismofomanual()
for manuels in b:
    time.sleep(3)
    print(manuels)

```
---
### How to install KaliLinux on windows
A short manual how to install KaliLinux for windows.

##### First check what type of operating System your windows has.

* 1.) Click with the left mouse button on the windows ⊞ logo on the bottom very left side where you shut down the PC and chose: "System" with the mouse, click
* 2.) if you have windows 10 or windows 11 there should be a description for your PCs' operating System. Example:
*  "System type:64-bit operating system, x64-based processor",
*  "productID : 0xxxx-0xxxx-0xxxx-XYZxxx" etc., --------- 
* 3.) We look for 64-bit / or 32-bit this will be your operating system

##### Download the thing

* 1.) Download virtualbox and extensions from virtualbox
* 2.) Download KaliLinux install package from their homepage
* 3.) Install Virtualbox and the hardware extensions for Mouse+Keyboard
* 4.) during the installation process give the VM 10GB space and 2GB processorspace to run a smooth VM on any cracklaptop
* 5.) When it comes to: <Chose "Operating System">: KaliLinux will not be displayed, just chose ubuntu64x or ubuntu32x depends on your windows- chose what we determined before
* 6.) You can chose between installing a downloaded package or importing a package, the differnce is the programtype:

If you downloaded the basic cali linux installer it should be a .iso file, If you have directly installed the VM package from their page it should be an .ovo file

* 7.) Just chose the right option for the Linux package you downloaded how described a line before
* 8.) Installation process goes very quick if you have the .ovo , the program just quickly installs all basic configurations as default (timezone, keyboard type etc etc.)
* 9.) To login into kali linux there is a small trick, the username and password by default are: username; kali - passphrase; kali

---
### useful link for symbols
Collection of Links I visit from time to time
[Unicodesymbols_Collection_for_Python](https://unicode-table.com/en/html-entities/)
