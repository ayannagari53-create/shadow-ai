; Script generated for S.H.A.D.O.W AI
; Non-commercial use only

#define MyAppName "S.H.A.D.O.W AI"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Ayan Nagari"
#define MyAppURL "https://shadow-ai-landing-page.vercel.app/"
#define MyAppExeName "ShadowAI.exe"
#define MyAppIconName "shadow.ico"

[Setup]
AppId={{CFDDECA2-D2C2-4324-8E27-5B85F63B662E}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}

DefaultDirName={autopf}\{#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

DisableProgramGroupPage=yes

OutputBaseFilename=ShadowAI-Setup

SetupIconFile=C:\Users\hp laptop\Desktop\SHADOWAI\dist\ShadowAI\shadow.ico

SolidCompression=yes
WizardStyle=modern dynamic

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
Source: "C:\Users\hp laptop\Desktop\SHADOWAI\dist\ShadowAI\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppIconName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; IconFilename: "{app}\{#MyAppIconName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent