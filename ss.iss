[Setup]
AppName=Img2Img Converter
AppVersion=1.0
DefaultDirName={pf}\Img2Img
OutputDir=.
OutputBaseFilename=Img2Img_Setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64
PrivilegesRequired=admin

[Files]
Source: "D:\Work\Coding\Python Projects\svg2ico\dist\img2img.exe"; DestDir: "{app}"
Source: "D:\Work\Coding\Python Projects\svg2ico\img2img.ico"; DestDir: "{app}"
; Include Pillow package
Source: "C:\Users\karan\AppData\Local\Programs\Python\Python312\Lib\site-packages\pillow-10.2.0.dist-info\*"; DestDir: "{app}\pillow-10.2.0.dist-info"

[Icons]
Name: "{group}\Img2Img Converter"; Filename: "{app}\img2img.exe"; IconFilename: "{app}\img2img.ico"
