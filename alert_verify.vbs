Set WshShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

' Set the working directory to your workspace path
Dim projectDir
projectDir = "C:\Users\trail\Independent Study Matrices"

If fso.FolderExists(projectDir) Then
    WshShell.CurrentDirectory = projectDir
    
    ' Run verify.bat invisibly (0 = hide window, True = wait for it to finish)
    Dim returnCode
    returnCode = WshShell.Run("cmd.exe /c verify.bat", 0, True)
    
    ' Trigger native Windows pop-up dialog boxes based on the exit return code
    If returnCode = 0 Then
        MsgBox "✔ INTEGRITY VERIFIED: All local research matrices match their cryptographic hashes. Your workspace is 100% secure.", 64, "Cryptographic Audit Success"
    Else
        MsgBox "🚨 SECURITY ALERT: Matrix verification failed! One or more spreadsheets have been tampered with or corrupted.", 16, "Data Integrity Violation"
    End If
Else
    MsgBox "Error: Project directory not found.", 48, "Path Error"
End If
